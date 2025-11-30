import os
import asyncio
from dotenv import load_dotenv # Import load_dotenv
load_dotenv() # Load environment variables from .env

from agents import Agent, Runner # Corrected import for Runner
from .math_functions import add as openai_add, subtract as openai_subtract # Import the decorated functions for OpenAI Agent
from .math_core import add, subtract # Import the core math functions for direct calling

from agents.extensions.models.litellm_model import LitellmModel # Import LitellmModel

# Configure the agent with the decorated math functions
math_agent = Agent(
    name="MathAgent",
    instructions="You are a helpful math assistant. Use the provided tools to perform addition and subtraction. Only perform math operations using the tools.",
    tools=[openai_add, openai_subtract], # Register the decorated functions as tools
    model=LitellmModel(model="gemini/gemini-2.0-flash-lite", api_key=os.environ.get("GEMINI_API_KEY")),  # Use LitellmModel for Gemini
)

async def chat_with_agent(user_query: str):
    """
    Initiates a chat with the math agent to process a natural language query.
    """
    try:
        # Use Runner.run to interact with the agent
        result = await Runner.run(math_agent, user_query)
        # The output of Runner.run is a RunResult object, its final output is in .output
        return str(result.final_output) # Convert to string for consistent return type in tests
    except Exception as e:
        # Basic error handling
        return f"Error: {e}"

# The old call_agent_function remains for direct programmatic access if needed.
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