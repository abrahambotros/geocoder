"""
Provides the simple LatLng model used throughout the rest of the app.
"""

# External imports
from typing import Any

# Internal imports
# - N/A


class LatLng(object):
    """
    Simple model for representing a (latitude, longitude) numeric 2-tuple.
    """

    def __init__(self, lat: float, lng: float) -> None:
        self.lat = lat
        self.lng = lng

    def __eq__(self, other: Any) -> bool:
        """
        Two LatLng (or one LatLng instance and one LatLng-like object) are
        considered equal if their lat and lng values are respectively equal.
        """
        return self.lat == other.lat and self.lng == other.lng
