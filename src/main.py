from fastapi import FastAPI
from pydantic import BaseModel
from src.agent.agent import chat_with_agent

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/chat")
async def chat(query: Query):
    """
    Receives a natural language query, sends it to the math agent, and returns the agent's response.
    """
    agent_response = await chat_with_agent(query.query)
    return {"response": agent_response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)