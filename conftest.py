# conftest.py
import logging
import pytest
import asyncio

def pytest_configure(config):
    """Configure pytest to suppress asyncio logging and handle LiteLLM event loop issues."""
    # Suppress verbose asyncio logging
    logging.getLogger("asyncio").setLevel(logging.WARNING)

    # LiteLLM's internal logging worker sometimes conflicts with pytest-asyncio's event loop management.
    # This RuntimeError: <Queue ...> is bound to a different event loop
    # indicates that LiteLLM's LoggingWorker is trying to use a different event loop
    # than the one pytest-asyncio provides for the tests.

    # Option 1: Try to disable LiteLLM's internal logging completely if possible (no direct config found yet)
    # Option 2: Ensure LiteLLM's worker uses the same event loop.

    # A common workaround for such RuntimeError in pytest-asyncio is to explicitly
    # set the default event loop policy at the start of tests, or to ensure that
    # tasks are created within the context of the pytest-asyncio managed loop.

    # For LiteLLM's internal worker, it's harder to control directly.
    # Let's try to set a general asyncio debug setting, it might reveal more.
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # This might help on Windows, but the root cause is still the Queue binding.
    
    # We will ignore the RuntimeError for now, as it is a non-fatal error related to the logging worker
    # and does not seem to prevent the actual tests from running their assertions correctly (except for the API quota).
    # If the tests pass despite this, we can consider it a known-issue with LiteLLM/pytest-asyncio interaction.
    pass

# We can define a fixture to ensure event loop is clean between tests if needed,
# but pytest-asyncio usually handles this well.
# @pytest.fixture(scope="session")
# def event_loop():
#     loop = asyncio.get_event_loop()
#     yield loop
#     loop.close()
