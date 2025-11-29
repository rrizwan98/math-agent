# Quickstart Guide: Math Agent

This guide provides a quick overview of how to interact with the Math Agent for basic addition and subtraction operations.

## Available Functions

The Math Agent exposes two primary functions:

1.  **`add(a: number, b: number)`**:
    *   **Description**: Returns the sum of two numbers, `a` and `b`.
    *   **Parameters**:
        *   `a` (number): The first operand.
        *   `b` (number): The second operand.
    *   **Returns**: The sum as a number.

2.  **`subtract(a: number, b: number)`**:
    *   **Description**: Returns the difference of two numbers, `a` and `b` (`a - b`).
    *   **Parameters**:
        *   `a` (number): The number to subtract from.
        *   `b` (number): The number to subtract.
    *   **Returns**: The difference as a number.

## Basic Usage Examples

*(Note: Actual invocation method will depend on the agent's integration layer, e.g., CLI, API call, function-calling API)*

### Example 1: Addition

To add `5` and `3`:

```
// Conceptual call (actual syntax may vary)
call_agent_function("add", 5, 3)
```

**Expected Output**: `8`

### Example 2: Subtraction

To subtract `7` from `10`:

```
// Conceptual call (actual syntax may vary)
call_agent_function("subtract", 10, 7)
```

**Expected Output**: `3`

### Example 3: Handling Decimal Numbers

```
call_agent_function("add", 1.5, 2.5)
// Expected Output: 4.0

call_agent_function("subtract", 10.5, 2.5)
// Expected Output: 8.0
```

## Error Handling

The agent will return a structured error message if invalid inputs are provided.

### Example 4: Invalid Input

```
call_agent_function("add", "hello", 5)
```

**Expected Output**: `{"error": "Invalid input: operands must be numbers"}` (exact message may vary)
