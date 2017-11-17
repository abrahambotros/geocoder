"""
Provides the simple LatLng model used throughout the rest of the app.
"""

# External imports
import json
from typing import Any, Dict

# Internal imports
# - N/A


class LatLng(object):
    """
    Simple model for representing a (latitude, longitude) numeric 2-tuple.
    """

    """
    API_FIELD_*'s define a specific mapping from implicit known fields on the
    model to enforced fields/keys in the information written back to any clients
    via the API.
    """
    API_FIELD_LAT = "lat"
    API_FIELD_LNG = "lng"

    def __init__(self, lat: float, lng: float) -> None:
        self.lat = lat
        self.lng = lng

    def __eq__(self, other: Any) -> bool:
        """
        Two LatLng (or one LatLng instance and one LatLng-like object) are
        considered equal if their lat and lng values are respectively equal.
        """
        return self.lat == other.lat and self.lng == other.lng

    def to_dict(self) -> Dict[str, float]:
        """
        Custom method for generating a Dict corresponding to a LatLng instance
        and its implicit properties.

        NOTE: We could also just do __dict__(), but choose this manual
            implementation in interests of clarity, control, and verbosity. This
            also would allow us to handle any property renaming when converting
            between raw model instance and dict representation.
        """
        return {
            LatLng.API_FIELD_LAT: self.lat,
            LatLng.API_FIELD_LNG: self.lng,
        }

    def to_json(self) -> str:
        """
        Custom method for generating a JSON string corresponding to a LatLng
        instance and its implicit properties. Wraps to_dict.

        NOTE: We could have also gone the JSONEncoder-subclassing route, but
            choose to manually implement this by wrapping toDict instead in the
            interests of clarity, control, and verbosity.
        """
        return json.dumps(self.to_dict())
