import pytest
from src.agent.agent import call_agent_function

def test_integration_add_valid_inputs():
    """
    Integration test for the conceptual /add endpoint with valid inputs.
    """
    assert call_agent_function("add", 2, 3) == 5.0
    assert call_agent_function("add", -10, 5) == -5.0
    assert call_agent_function("add", 1.5, 2.5) == 4.0

def test_integration_subtract_valid_inputs():
    """
    Integration test for the conceptual /subtract endpoint with valid inputs.
    """
    assert call_agent_function("subtract", 5, 3) == 2.0
    assert call_agent_function("subtract", 3, 5) == -2.0
    assert call_agent_function("subtract", 10.5, 2.5) == 8.0

def test_integration_add_non_numeric_inputs():
    """
    Integration test for the conceptual /add endpoint with non-numeric inputs.
    """
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        call_agent_function("add", "a", 3)

def test_integration_subtract_non_numeric_inputs():
    """
    Integration test for the conceptual /subtract endpoint with non-numeric inputs.
    """
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        call_agent_function("subtract", 5, "b")
