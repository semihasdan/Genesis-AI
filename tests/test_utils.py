"""
Test cases for utility functions.
"""

import pytest
from src.utils import calculate_factorial


def test_calculate_factorial():
    """Test the calculate_factorial function."""
    # Test base cases
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    
    # Test normal cases
    assert calculate_factorial(5) == 120
    
    # Test edge cases
    with pytest.raises(ValueError):
        calculate_factorial(-1)
