"""
Controller file implementing geocoding requests to the Google Maps Geocoding
API.
"""

# External imports
from typing import Any

# Internal imports
from app.models.lat_lng import LatLng


def geocode(address: str) -> LatLng:
    """
    Geocode the given address string to (lat, lng) coordinates, by making a
    manual HTTP request to the Google Maps Geocoding API.

    TODO: Implement.
    """
    return LatLng(lat=0, lng=0)
