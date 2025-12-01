# src/agent/math_functions.py
from agents import function_tool
from .math_core import add as core_add, subtract as core_subtract

@function_tool
def add(a: float, b: float) -> float:
    """
    Adds two numbers together.
    :param a: The first number to add.
    :param b: The second number to add.
    """
    return core_add(a, b)

@function_tool
def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first number.
    :param a: The number to subtract from.
    :param b: The number to subtract.
    """
    return core_subtract(a, b)
