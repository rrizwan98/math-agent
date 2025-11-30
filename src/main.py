from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # Import StaticFiles
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
from pydantic import BaseModel
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

@app.get("/")
async def read_root():
    return {"message": "Math Agent FastAPI is running!"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = await chat_with_agent(request.query)
    return {"response": response}

# Mount static files for the frontend
app.mount("/app", StaticFiles(directory="frontend/dist", html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)