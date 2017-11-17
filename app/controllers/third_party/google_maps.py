"""
Controller file implementing geocoding requests to the Google Maps Geocoding
API.
"""

# External imports
import json
import ssl
import urllib.request
from urllib.parse import urlencode
from typing import Dict

# Internal imports
from app.models.lat_lng import LatLng
from app.conf.settings import GMAPS_API_KEY

# Constants
_URL_GEOCODE_BASE = "https://maps.googleapis.com/maps/api/geocode/json"
_URL_PARAM_ADDRESS = "address"
_URL_PARAM_API_KEY = "key"


def geocode(address: str) -> LatLng:
    """
    Geocode the given address string to (lat, lng) coordinates, by making a
    manual HTTP request to the Google Maps Geocoding API.

    TODO: Implement.
    TODO: Handle errors.
    """
    # Build URL params dict for request, with address string and Google Maps API
    # key from settings.
    params_dict: Dict[str, str] = {
        _URL_PARAM_ADDRESS: address,
        _URL_PARAM_API_KEY: GMAPS_API_KEY,
    }

    # URL-encode the URL params dict into a URL-encoded string.
    params_str: str = urlencode(params_dict)

    # Fire off the request to the Google Maps Geocoding API. Parse response to
    # JSON dict.
    url = "%s?%s" % (_URL_GEOCODE_BASE, params_str)
    # TODO: Python 3's increased SSL security for requests will likely cause a
    #    CERTIFICATE_VERIFY_FAILED error on most local systems without elaborate
    #    certificate setup. Because of this, we currently disable SSL
    #    verification of the CONTROLLED requests we make to the known API
    #    endpoints via the explicit context setting below.
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url=url, context=context) as resp:
        resp_data = json.loads(resp.read().decode("utf-8"))

    # Parse response data latitude and longitude into LatLng instance.
    print(resp_data, type(resp_data))

    # Return created LatLng instance with success.
    # TODO: Use real instance instead of placeholder.
    return LatLng(lat=0, lng=0)
