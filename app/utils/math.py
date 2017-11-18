"""
Math utils.
"""

# External imports
from typing import Union

# Internal imports
# - N/A


def equalish(x: Union[int, float], y: Union[int, float], precision_digits: int = 7) -> bool:
    """
    Given two numeric values, determine if they are "equalish" - meaning they
    are equal up to some given numeric precision (given by precision_digits).
    """
    return round(x - y, ndigits=precision_digits) == 0
