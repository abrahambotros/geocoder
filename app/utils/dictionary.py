"""
Dictionary/dict utils.
"""

# External imports
from typing import Any, Dict, List

# Internal imports
# - N/A


def get_nested_value(dictionary: Dict, keys: List[Any], default: Any = None) -> Any:
    """
    Given a dict and a list of keys, descend into the dict via the keys in
    order. If the corresponding key for a level is not found in the sub-dict at
    that level, then return the default value. Return the value at the nested
    location reached by descending levels in the order of the keys.
    """
    val = dictionary
    for key in keys:
        if key not in val:
            return default
        val = val[key]
    return val
