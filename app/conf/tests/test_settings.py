"""
Tests for settings.
"""

# External imports
import unittest

# Internal imports
from app.conf import settings


class TestSettings(unittest.TestCase):

    def test_gmaps_api_key(self):
        self.assertTrue(settings.GMAPS_API_KEY, "Missing Google Maps API key")

    def test_here_app_id(self):
        self.assertTrue(settings.HERE_APP_ID, "Missing HERE app id")

    def test_here_app_code(self):
        self.assertTrue(settings.HERE_APP_CODE, "Missing HERE app code")
