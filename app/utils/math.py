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

    Args:
        x: Number to compare.
        y: Number to compare.
        precision_digits: Int indicating the precision as the number of digits
            after the decimal point that we will use to determine equality.
            Functions according to the ndigits parameter in the built-in `round`
            function, which we wrap here.

    Returns:
        True if x and y are "equal"-ish, as defined above; False otherwise.
    """
    return round(x - y, ndigits=precision_digits) == 0
