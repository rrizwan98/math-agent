from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from starlette.middleware.base import BaseHTTPMiddleware

from src.agent.agent import chat_with_agent

class ChatRequest(BaseModel):
    query: str

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Add CSP middleware to allow unsafe-eval for ChatKit
class CSPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        # Add CSP header that allows unsafe-eval for ChatKit compatibility
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-eval' 'unsafe-inline' https:; "
            "style-src 'self' 'unsafe-inline' https:; "
            "img-src 'self' data: https:; "
            "font-src 'self' data: https:; "
            "connect-src 'self' http://localhost:8000 https:;"
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

# Define the path to your frontend's dist directory
frontend_dist_path = Path(__file__).parent / ".." / "frontend" / "dist"

# Mount static files for the frontend assets
app.mount("/app/assets", StaticFiles(directory=frontend_dist_path / "assets"), name="frontend_assets")

# Explicitly serve index.html for the /app/ and /app paths
@app.get("/app", response_class=HTMLResponse)
@app.get("/app/", response_class=HTMLResponse)
async def serve_frontend():
    with open(frontend_dist_path / "index.html", "r", encoding="utf-8") as f:
        return f.read()

# Serve vite.svg directly if needed
app.mount("/app/vite.svg", StaticFiles(directory=frontend_dist_path), name="frontend_vite_svg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
