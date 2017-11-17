"""
Controller file implementing geocoding requests to the Google Maps Geocoding
API.
"""

# External imports
# - N/A

# Internal imports
from app.models.lat_lng import LatLng


def geocode(address: str) -> LatLng:
    """
    Geocode the given address string to (lat, lng) coordinates, by making a
    manual HTTP request to the Google Maps Geocoding API.

    TODO: Implement.
    TODO: Handle errors.
    """
    # Build URL params dict for request, with address string and Google Maps API
    # key from settings.

    # URL-encode the URL params dict into a URL-encoded string.

    # Fire off the request to the Google Maps Geocoding API.

    # Parse response latitude and longitude into LatLng instance.

    # Return created LatLng instance with success.
    # TODO: Use real instance instead of placeholder.
    return LatLng(lat=0, lng=0)
