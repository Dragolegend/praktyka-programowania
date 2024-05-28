"""
This module provides basic arithmetic operations.

Functions:
- add(a: int, b: int) -> int: Returns the sum of a and b.
- subtract(a: int, b: int) -> int: Returns the difference when b is subtracted from a.
- multiply(a: int, b: int) -> int: Returns the product of a and b.
- divide(a: int, b: int) -> float: Returns the division of a by b.
"""

# przykladowe funkcje utils.py

def add(a: int, b: int) -> int:
    """
    Returns the sum of two integers.
    
    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.
    
    Returns:
    int: The sum of a and b.
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Returns the difference between two integers.
    
    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.
    
    Returns:
    int: The difference between a and b.
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    Returns the product of two integers.
    
    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.
    
    Returns:
    int: The product of a and b.
    """
    return a * b

def divide(a: int, b: int) -> float:
    """
    Returns the result of dividing the first integer by the second integer.
    
    Parameters:
    - a (int): The numerator.
    - b (int): The denominator.
    
    Returns:
    float: The result of dividing a by b.
    """
    return a / b
