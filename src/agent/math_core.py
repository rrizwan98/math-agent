# src/agent/math_core.py

from ..lib.validation import is_numeric

def add(a: float, b: float) -> float:
    """
    Adds two numbers.
    """
    if not (is_numeric(a) and is_numeric(b)):
        raise ValueError("Inputs must be numbers.")
    return float(a + b)

def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first number.
    """
    if not (is_numeric(a) and is_numeric(b)):
        raise ValueError("Inputs must be numbers.")
    return float(a - b)
