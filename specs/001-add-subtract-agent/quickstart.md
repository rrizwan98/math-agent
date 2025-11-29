# Quickstart Guide: Math Agent with OpenAI SDK

This guide provides a quick overview of how to interact with the Math Agent for basic addition and subtraction operations using natural language via the OpenAI Agent SDK.

## Available Functions (as tools for the OpenAI Agent)

The Math Agent exposes two primary functions as tools for the OpenAI Agent:

1.  **`add(a: number, b: number)`**:
    *   **Description**: Adds two numbers, `a` and `b`.
    *   **Parameters**:
        *   `a` (number): The first operand.
        *   `b` (number): The second operand.
    *   **Returns**: The sum as a number.

2.  **`subtract(a: number, b: number)`**:
    *   **Description**: Subtracts one number from another, `a` and `b` (`a - b`).
    *   **Parameters**:
        *   `a` (number): The number to subtract from.
        *   `b` (number): The number to subtract.
    *   **Returns**: The difference as a number.

## Basic Usage Examples (via Natural Language)

To interact with the agent, you will use the `chat_with_agent` asynchronous function, providing a natural language query.

### Example 1: Addition

To add `5` and `3` using natural language:

```python
import asyncio
from src.agent.agent import chat_with_agent

async def main():
    query = "Please add 5 and 3 for me."
    result = await chat_with_agent(query)
    print(result)

if __name__ == "__main__":
    # Ensure OPENAI_API_KEY environment variable is set.
    # e.g., export OPENAI_API_KEY="YOUR_API_KEY"
    asyncio.run(main())
```

**Expected Output**: `8.0`

### Example 2: Subtraction

To subtract `7` from `10` using natural language:

```python
import asyncio
from src.agent.agent import chat_with_agent

async def main():
    query = "What is 10 minus 7?"
    result = await chat_with_agent(query)
    print(result)

if __name__ == "__main__":
    # Ensure OPENAI_API_KEY environment variable is set.
    # e.g., export OPENAI_API_KEY="YOUR_API_KEY"
    asyncio.run(main())
```

**Expected Output**: `3.0`

### Example 3: Handling Decimal Numbers

```python
import asyncio
from src.agent.agent import chat_with_agent

async def main():
    query_add = "Add 1.5 to 2.5"
    result_add = await chat_with_agent(query_add)
    print(f"Add result: {result_add}") # Expected: 4.0

    query_subtract = "Take 2.5 away from 10.5"
    result_subtract = await chat_with_agent(query_subtract)
    print(f"Subtract result: {result_subtract}") # Expected: 8.0

if __name__ == "__main__":
    # Ensure OPENAI_API_KEY environment variable is set.
    # e.g., export OPENAI_API_KEY="YOUR_API_KEY"
    asyncio.run(main())
```

## Error Handling (via Natural Language)

The agent will return a structured error message if invalid inputs are provided or unsupported operations are requested via natural language.

### Example 4: Invalid Input

```python
import asyncio
from src.agent.agent import chat_with_agent

async def main():
    query = "Can you add 'hello' and 3?"
    result = await chat_with_agent(query)
    print(result)

if __name__ == "__main__":
    # Ensure OPENAI_API_KEY environment variable is set.
    # e.g., export OPENAI_API_KEY="YOUR_API_KEY"
    asyncio.run(main())
```

**Expected Output**: An error message indicating invalid input (e.g., "Error: Inputs must be numbers." or a model-generated response indicating it can't perform the action with non-numeric inputs).

### Example 5: Unsupported Operation

```python
import asyncio
from src.agent.agent import chat_with_agent

async def main():
    query = "What is 2 multiplied by 3?"
    result = await chat_with_agent(query)
    print(result)

if __name__ == "__main__":
    # Ensure OPENAI_API_KEY environment variable is set.
    # e.g., export OPENAI_API_KEY="YOUR_API_KEY"
    asyncio.run(main())
```

**Expected Output**: A response indicating the operation is not supported (e.g., "I can only add and subtract numbers.").