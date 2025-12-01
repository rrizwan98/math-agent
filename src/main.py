from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from src.agent.agent import chat_with_agent
from src.chatkit_store import InMemoryStore
from chatkit.server import ChatKitServer, StreamingResult, NonStreamingResult
from chatkit.types import ThreadMetadata, UserMessageItem
from typing import AsyncIterator, Any
import json

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MyChatKitServer(ChatKitServer):
    def __init__(self, store):
        super().__init__(store=store)

    async def respond(
        self, 
        thread: ThreadMetadata, 
        input_user_message: UserMessageItem | None, 
        context: Any
    ) -> AsyncIterator[Any]:
        """Handle user messages by calling the math agent."""
        from chatkit.types import ThreadItemAddedEvent, ThreadItemDoneEvent, AssistantMessageItem, AssistantMessageContent
        from datetime import datetime
        import uuid
        
        # Get the user query from the input message
        if input_user_message and input_user_message.content:
            # Extract text from the first content block
            for content_block in input_user_message.content:
                if hasattr(content_block, 'text'):
                    user_query = content_block.text
                    break
            else:
                user_query = "Hello"
        else:
            user_query = "Hello"

        # Get response from the agent
        agent_response = await chat_with_agent(user_query)
        
        # Create an assistant message with the response
        msg_id = f"msg_{uuid.uuid4().hex[:12]}"
        content_block = AssistantMessageContent(type="output_text", text=agent_response)
        assistant_msg = AssistantMessageItem(
            id=msg_id,
            thread_id=thread.id,
            created_at=datetime.now(),
            type="assistant_message",
            content=[content_block]
        )
        
        # Yield the item added event
        yield ThreadItemAddedEvent(type="thread.item.added", item=assistant_msg)
        
        # Yield the item done event
        yield ThreadItemDoneEvent(type="thread.item.done", item=assistant_msg)


# Initialize ChatKit store
store = InMemoryStore()

# Initialize ChatKit server
chatkit_server = MyChatKitServer(store)


# ChatKit API endpoint
@app.post("/chatkit")
async def chatkit_endpoint(request: Request):
    """Handle ChatKit API requests."""
    # Read the raw body
    body = await request.body()
    
    # Process the request using ChatKit server
    result = await chatkit_server.process(body, context=None)
    
    # Check if it's a streaming result
    if isinstance(result, StreamingResult):
        async def generate():
            async for chunk in result:
                yield chunk
        
        return StreamingResponse(
            generate(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Access-Control-Allow-Origin": "*",
            }
        )
    else:
        # Non-streaming result - return as JSON
        return Response(
            content=result.json,
            media_type="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
