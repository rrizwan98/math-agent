import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner
from .math_functions import add as openai_add, subtract as openai_subtract
from .math_core import add, subtract

from agents.extensions.models.litellm_model import LitellmModel

math_agent = Agent(
    name="MathAgent",
    instructions="You are a helpful math assistant. Use the provided tools to perform addition and subtraction. Only perform math operations using the tools.",
    tools=[openai_add, openai_subtract],
    model=LitellmModel(model="gemini/gemini-2.0-flash-lite", api_key=os.environ.get("GEMINI_API_KEY")),
)

async def chat_with_agent(user_query: str):
    """
    Initiates a chat with the math agent to process a natural language query.
    """
    try:
        # Introduce a 30-second non-blocking delay for every Gemini API call
        await asyncio.sleep(30) # <<< ADDED THIS LINE

        result = await Runner.run(math_agent, user_query)
        return str(result.final_output)
    except Exception as e:
        return f"Error: {e}"

def call_agent_function(function_name, *args):
    """
    Conceptual agent interface for calling math functions directly.
    """
    if function_name == "add":
        return add(*args)
    elif function_name == "subtract":
        return subtract(*args)
    else:
        raise ValueError(f"Unknown function: {function_name}")
