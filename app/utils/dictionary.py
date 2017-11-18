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

    Args:
        dictionary: Dictionary (possibly with nested keys/values) that we want
            to access for lookup.
        keys: List of keys (in order) we will use to traverse/descend into the
            (nested) structure of the given dictionary.
        default: Default value to use if no matching value was found after
            traversing/descending into the dictionary according to keys.

    Returns:
        Value inside dictionary reached by traversing/descending into the
        dictionary according to the ordered keys. If not found, then this is
        the given default value instead.
    """
    val = dictionary
    for key in keys:
        if key not in val:
            return default
        val = val[key]
    return val
