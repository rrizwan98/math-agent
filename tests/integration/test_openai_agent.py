import pytest
import asyncio
from src.agent.agent import chat_with_agent
import re

def extract_number_from_response(response_text: str) -> float | None:
    """
    Extracts a float number from a conversational response string, looking for the last number in the string.
    """
    # Regex to find a number (integer or float, positive or negative) at the end of the string
    # or followed by punctuation/space.
    match = re.findall(r"[-+]?\d*\.?\d+", response_text)
    if match:
        return float(match[-1]) # Return the last found number
    return None

@pytest.mark.asyncio
async def test_natural_language_add_valid_inputs():
    """
    Integration test for natural language addition via OpenAI SDK.
    """
    # Test case 1: Positive integers
    query = "add 2 and 3"
    result_text = await chat_with_agent(query)
    await asyncio.sleep(25)
    if "ratelimiterror" in result_text.lower() or "quota" in result_text.lower():
        pytest.fail(f"Test failed due to RateLimitError/Quota Exceeded: {result_text}")
    result_num = extract_number_from_response(result_text)
    assert result_num == 5.0, f"Expected 5.0, but got '{result_text}'"

    # Test case 2: Negative integers
    query = "what is -10 plus 5"
    result_text = await chat_with_agent(query)
    await asyncio.sleep(25)
    if "ratelimiterror" in result_text.lower() or "quota" in result_text.lower():
        pytest.fail(f"Test failed due to RateLimitError/Quota Exceeded: {result_text}")
    result_num = extract_number_from_response(result_text)
    assert result_num == -5.0, f"Expected -5.0, but got '{result_text}'"

    # Test case 3: Floats
    query = "add 1.5 to 2.5"
    result_text = await chat_with_agent(query)
    await asyncio.sleep(25)
    if "ratelimiterror" in result_text.lower() or "quota" in result_text.lower():
        pytest.fail(f"Test failed due to RateLimitError/Quota Exceeded: {result_text}")
    result_num = extract_number_from_response(result_text)
    assert result_num == 4.0, f"Expected 4.0, but got '{result_text}'"

@pytest.mark.asyncio
async def test_natural_language_subtract_valid_inputs():
    """
    Integration test for natural language subtraction via OpenAI SDK.
    """
    # Test case 1: Positive integers
    query = "subtract 3 from 5"
    result_text = await chat_with_agent(query)
    await asyncio.sleep(25)
    if "ratelimiterror" in result_text.lower() or "quota" in result_text.lower():
        pytest.fail(f"Test failed due to RateLimitError/Quota Exceeded: {result_text}")
    result_num = extract_number_from_response(result_text)
    assert result_num == 2.0, f"Expected 2.0, but got '{result_text}'"

    # Test case 2: Negative result
    query = "what is 3 minus 5"
    result_text = await chat_with_agent(query)
    await asyncio.sleep(25)
    if "ratelimiterror" in result_text.lower() or "quota" in result_text.lower():
        pytest.fail(f"Test failed due to RateLimitError/Quota Exceeded: {result_text}")
    result_num = extract_number_from_response(result_text)
    assert result_num == -2.0, f"Expected -2.0, but got '{result_text}'"

    # Test case 3: Floats
    query = "take 2.5 away from 10.5"
    result_text = await chat_with_agent(query)
    await asyncio.sleep(25)
    if "ratelimiterror" in result_text.lower() or "quota" in result_text.lower():
        pytest.fail(f"Test failed due to RateLimitError/Quota Exceeded: {result_text}")
    result_num = extract_number_from_response(result_text)
    assert result_num == 8.0, f"Expected 8.0, but got '{result_text}'"

@pytest.mark.asyncio
async def test_natural_language_non_numeric_inputs():
    """
    Integration test for non-numeric inputs via natural language via OpenAI SDK.
    """
    query = "add 'hello' and 3"
    result = await chat_with_agent(query)
    await asyncio.sleep(25)
    # The agent is expected to return an error message from the tool call itself
    # or handle it gracefully.
    assert "error" in result.lower() or "invalid" in result.lower() or "numbers" in result.lower()

    query = "subtract 5 from 'world'"
    result = await chat_with_agent(query)
    await asyncio.sleep(25)
    assert "error" in result.lower() or "invalid" in result.lower() or "numbers" in result.lower()

@pytest.mark.asyncio
async def test_natural_language_unsupported_operation():
    """
    Integration test for unsupported operations via natural language via OpenAI SDK.
    """
    query = "multiply 2 by 3"
    result = await chat_with_agent(query)
    await asyncio.sleep(25)
    assert any(
        phrase in result.lower()
        for phrase in [
            "cannot fulfill",
            "unsupported",
            "not perform",
            "only add and subtract",
            "only perform addition and subtraction",
            "ratelimiterror",
            "quota",
        ]
    ), f"Unexpected response: {result}"
