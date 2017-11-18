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
                dictionary=d, keys=["one", "two", 3, "four"], default=None),
            4,
        )
        self.assertEqual(
            utils_dictionary.get_nested_value(
                dictionary=d, keys=["one", "five"], default=None),
            5,
        )
        self.assertEqual(
            utils_dictionary.get_nested_value(
                dictionary=d, keys=["one", "not present"], default=100),
            100,
        )
