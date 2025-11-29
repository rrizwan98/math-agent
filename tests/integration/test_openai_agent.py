import pytest
import asyncio
from src.agent.agent import chat_with_agent

@pytest.mark.asyncio
async def test_natural_language_add_valid_inputs():
    """
    Integration test for natural language addition via OpenAI SDK.
    """
    # Test case 1: Positive integers
    query = "add 2 and 3"
    result = await chat_with_agent(query)
    assert result == "5.0"

    # Test case 2: Negative integers
    query = "what is -10 plus 5"
    result = await chat_with_agent(query)
    assert result == "-5.0"

    # Test case 3: Floats
    query = "add 1.5 to 2.5"
    result = await chat_with_agent(query)
    assert result == "4.0"

@pytest.mark.asyncio
async def test_natural_language_subtract_valid_inputs():
    """
    Integration test for natural language subtraction via OpenAI SDK.
    """
    # Test case 1: Positive integers
    query = "subtract 3 from 5"
    result = await chat_with_agent(query)
    assert result == "2.0"

    # Test case 2: Negative result
    query = "what is 3 minus 5"
    result = await chat_with_agent(query)
    assert result == "-2.0"

    # Test case 3: Floats
    query = "take 2.5 away from 10.5"
    result = await chat_with_agent(query) # Corrected typo here
    assert result == "8.0"

@pytest.mark.asyncio
async def test_natural_language_non_numeric_inputs():
    """
    Integration test for non-numeric inputs via natural language via OpenAI SDK.
    """
    query = "add 'hello' and 3"
    result = await chat_with_agent(query)
    # The agent is expected to return an error message from the tool call itself
    # or handle it gracefully. The exact output might vary based on OpenAI's model
    # response when it fails to call a tool with invalid parameters.
    # For now, we expect it to indicate an error related to invalid input types.
    assert "error" in result.lower() or "invalid" in result.lower()

    query = "subtract 5 from 'world'"
    result = await chat_with_agent(query)
    assert "error" in result.lower() or "invalid" in result.lower()

@pytest.mark.asyncio
async def test_natural_language_unsupported_operation():
    """
    Integration test for unsupported operations via natural language via OpenAI SDK.
    """
    query = "multiply 2 by 3"
    result = await chat_with_agent(query)
    # The agent is not designed to perform multiplication, so it should
    # respond that it cannot fulfill the request or indicate unsupported operation.
    assert "cannot fulfill" in result.lower() or "unsupported" in result.lower() or "not perform" in result.lower()
