"""
Main controller providing a simple interface for API requests to geocode based
on an input address string. Abstracts away callers from having to interact with
third-party geocoding service requests and backup/fallback logic.
"""

# External imports
from typing import Any

# Internal imports
from app.models.lat_lng import LatLng


def geocode(address: str) -> LatLng:
    """
    Geocode the given address string to (lat, lng) coordinates.

    TODO: Implement.
    TODO: Document.
    """
    return LatLng(lat=0, lng=0)
