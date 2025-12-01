from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
import json
import uuid

from src.agent.agent import chat_with_agent
from src.chatkit_store import InMemoryStore

class ChatRequest(BaseModel):
    query: str

app = FastAPI()

# Initialize ChatKit store
store = InMemoryStore()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add CSP middleware to allow unsafe-eval for ChatKit
class CSPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-eval' 'unsafe-inline' https:; "
            "style-src 'self' 'unsafe-inline' https:; "
            "img-src 'self' data: https:; "
            "font-src 'self' data: https:; "
            "connect-src 'self' http://localhost:8000 http://127.0.0.1:8000 https:;"
        )
        return response

app.add_middleware(CSPMiddleware)

@app.get("/")
async def read_root():
    return {"message": "Math Agent FastAPI is running!"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = await chat_with_agent(request.query)
    return {"response": response}

# ChatKit API endpoint
@app.post("/chatkit")
async def chatkit_endpoint(request: Request):
    """Handle ChatKit API requests with SSE streaming."""
    body = await request.json()
    
    async def generate_sse():
        try:
            action = body.get("action", "")
            
            if action == "threads.create":
                thread_id = f"thr_{uuid.uuid4().hex[:8]}"
                thread_data = {
                    "id": thread_id,
                    "title": "New Chat",
                    "created_at": datetime.now().isoformat(),
                    "updated_at": datetime.now().isoformat(),
                }
                yield f"data: {json.dumps({'type': 'thread.created', 'thread': thread_data})}\n\n"
                
            elif action == "threads.list":
                threads = await store.load_threads(limit=20, after=None, order="desc", context=None)
                event_data = {
                    "type": "threads.list",
                    "threads": [
                        {
                            "id": t.id,
                            "title": t.title,
                            "created_at": t.created_at.isoformat() if t.created_at else None,
                            "updated_at": t.updated_at.isoformat() if t.updated_at else None,
                        }
                        for t in threads.data
                    ],
                    "has_more": threads.has_more
                }
                yield f"data: {json.dumps(event_data)}\n\n"
                
            elif action == "threads.addUserMessage":
                thread_id = body.get("thread_id")
                message = body.get("message", {})
                user_text = message.get("content", "")
                
                if not thread_id:
                    thread_id = f"thr_{uuid.uuid4().hex[:8]}"
                    thread_data = {
                        "id": thread_id,
                        "title": user_text[:50] if user_text else "New Chat",
                        "created_at": datetime.now().isoformat(),
                        "updated_at": datetime.now().isoformat(),
                    }
                    yield f"data: {json.dumps({'type': 'thread.created', 'thread': thread_data})}\n\n"
                
                user_msg_id = f"msg_{uuid.uuid4().hex[:8]}"
                yield f"data: {json.dumps({'type': 'thread.item.added', 'item': {'id': user_msg_id, 'type': 'user_message', 'content': [{'type': 'text', 'text': user_text}]}})}\n\n"
                
                response_text = await chat_with_agent(user_text)
                
                assistant_msg_id = f"msg_{uuid.uuid4().hex[:8]}"
                yield f"data: {json.dumps({'type': 'thread.item.added', 'item': {'id': assistant_msg_id, 'type': 'assistant_message', 'content': []}})}\n\n"
                yield f"data: {json.dumps({'type': 'thread.item.content_part.added', 'item_id': assistant_msg_id, 'part': {'type': 'text', 'text': ''}})}\n\n"
                yield f"data: {json.dumps({'type': 'thread.item.content_part.text.delta', 'item_id': assistant_msg_id, 'part_index': 0, 'delta': response_text})}\n\n"
                yield f"data: {json.dumps({'type': 'thread.item.content_part.done', 'item_id': assistant_msg_id, 'part_index': 0})}\n\n"
                yield f"data: {json.dumps({'type': 'thread.item.done', 'item': {'id': assistant_msg_id, 'type': 'assistant_message', 'content': [{'type': 'text', 'text': response_text}]}})}\n\n"
                
            else:
                yield f"data: {json.dumps({'type': 'stream.options', 'options': {}})}\n\n"
                
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'error': {'message': str(e)}})}\n\n"
        
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(
        generate_sse(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

# Define the path to your frontend's dist directory
frontend_dist_path = Path(__file__).parent.parent / "frontend" / "dist"
frontend_dist_path = frontend_dist_path.resolve()

# Mount static files for the frontend assets
app.mount("/app/assets", StaticFiles(directory=str(frontend_dist_path / "assets")), name="frontend_assets")

# Serve vite.svg directly if needed
app.mount("/app/vite.svg", StaticFiles(directory=str(frontend_dist_path)), name="frontend_vite_svg")

# Explicitly serve index.html for the /app/ and /app paths
@app.get("/app", response_class=HTMLResponse)
@app.get("/app/", response_class=HTMLResponse)
async def serve_frontend():
    index_path = frontend_dist_path / "index.html"
    if not index_path.exists():
        return HTMLResponse(content="<h1>Frontend not found. Please build the frontend first.</h1>", status_code=404)
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
