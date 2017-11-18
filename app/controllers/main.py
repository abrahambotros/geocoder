"""
Main controller providing a simple interface for API requests to geocode based
on an input address string. Abstracts away callers from having to interact with
third-party geocoding service requests and backup/fallback logic.
"""

# External imports
# - N/A

# Internal imports
from app.controllers.third_party import google_maps as gmaps_controller
from app.models.lat_lng import LatLng


def geocode(address: str) -> LatLng:
    """
    Geocode the given address string to (lat, lng) coordinates.

    TODO: Implement fallback.
    TODO: Document. Note throws exception.
    """
    try:
        return gmaps_controller.geocode(address=address)
    except Exception:
        raise RuntimeError("Error geocoding address: %s" % address)
