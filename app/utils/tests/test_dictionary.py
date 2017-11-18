"""
Tests for dict utils.
"""

# External imports
import unittest

# Internal imports
from app.utils import dictionary as utils_dictionary


class TestUtilsDictionary(unittest.TestCase):

    def test_get_nested_value(self):
        d = {
            "one": {
                "two": {
                    3: {
                        "four": 4,
                    },
                },
                "five": 5,
            },
        }
        self.assertEqual(
            utils_dictionary.get_nested_value(
                d=d, keys=["one", "two", 3, "four"]),
            4,
        )
        self.assertEqual(
            utils_dictionary.get_nested_value(d=d, keys=["one", "five"]),
            5,
        )
