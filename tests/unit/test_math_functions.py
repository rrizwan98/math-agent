import pytest
from src.agent.math_core import add, subtract

# Unit tests for add function
def test_add_positive_integers():
    assert add(2, 3) == 5.0

def test_add_negative_integers():
    assert add(-10, 5) == -5.0

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_zero():
    assert add(0, 0) == 0.0
    assert add(5, 0) == 5.0
    assert add(0, -5) == -5.0

# Unit tests for subtract function
def test_subtract_positive_integers():
    assert subtract(5, 3) == 2.0

def test_subtract_negative_integers():
    assert subtract(3, 5) == -2.0

def test_subtract_floats():
    assert subtract(10.5, 2.5) == 8.0

def test_subtract_zero():
    assert subtract(5, 0) == 5.0
    assert subtract(0, 5) == -5.0

# Unit tests for add function with non-numeric inputs
def test_add_non_numeric_input_a():
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        add("a", 3)

def test_add_non_numeric_input_b():
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        add(5, "b")

# Unit tests for subtract function with non-numeric inputs
def test_subtract_non_numeric_input_a():
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        subtract("a", 3)

def test_subtract_non_numeric_input_b():
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        subtract(5, "b")
