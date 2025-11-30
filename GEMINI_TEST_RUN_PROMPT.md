# Instructions for Running Tests with Pytest

## Project Setup
This is a Python project that uses `uv` for dependency management. The project is located at: `C:\Users\HP\Desktop\spec-driven-development\math-agent`

## How to Run Tests

### Prerequisites
1. Make sure you are in the project root directory: `C:\Users\HP\Desktop\spec-driven-development\math-agent`
2. Ensure dependencies are installed: Run `uv sync` if needed

### Running All Tests
To run all tests in the project, use this command:
```bash
uv run pytest tests/ -v
```

### Running Specific Test Files
To run a specific test file:
```bash
uv run pytest tests/integration/test_openai_agent.py -v
```

To run a specific test function:
```bash
uv run pytest tests/integration/test_openai_agent.py::test_natural_language_add_valid_inputs -v
```

### Running Tests with More Details
To see more detailed output including print statements:
```bash
uv run pytest tests/ -v -s
```

## Important Notes

1. **Use `uv run pytest`** - Do NOT use `pytest` directly. Always prefix with `uv run` to ensure the correct virtual environment is used.

2. **Test Structure**:
   - Unit tests are in: `tests/unit/`
   - Integration tests are in: `tests/integration/`

3. **Expected Behavior**:
   - All tests should pass (20 tests total)
   - You may see warnings from third-party libraries (Pydantic deprecation warnings) - these are normal and can be ignored
   - If you see `RateLimitError` or `Quota Exceeded` errors, it means the Gemini API quota has been exceeded - wait a few minutes and try again

4. **Common Commands**:
   - `uv run pytest tests/ -v` - Run all tests with verbose output
   - `uv run pytest tests/integration/ -v` - Run only integration tests
   - `uv run pytest tests/unit/ -v` - Run only unit tests

## Example Output
When tests pass successfully, you should see:
```
============================= test session starts =============================
...
======================== 20 passed, X warnings in Y.YYs =======================
```

If tests fail, you'll see detailed error messages indicating which test failed and why.

