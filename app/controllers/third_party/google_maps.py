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
from app.utils import dictionary as utils_dictionary

# Constants
_URL_GEOCODE_BASE = "https://maps.googleapis.com/maps/api/geocode/json"
_URL_PARAM_ADDRESS = "address"
_URL_PARAM_API_KEY = "key"


def geocode(address: str) -> LatLng:
    """
    Geocode the given address string to (lat, lng) coordinates, by making a
    manual HTTP request to the Google Maps Geocoding API.
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
    # TODO: Handle errors.
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url=url, context=context) as resp:
        resp_dict = json.loads(resp.read().decode("utf-8"))

    # Parse response data dict's latitude and longitude into LatLng instance and
    # return with success. If error, raise exception.
    try:
        return _parse_geocode_response_dict_to_lat_lng(resp_dict)
    except Exception:
        raise RuntimeError("Error parsing Google Maps Geocoding API response")


def _parse_geocode_response_dict_to_lat_lng(d: Dict) -> LatLng:
    """
    TODO: Document. Raises exception.
    """
    # If invalid input, raise error.
    if not d:
        raise ValueError("Invalid empty input dict")

    # Get top-level result from results list.
    results = d["results"]
    if not results:
        raise ValueError("Invalid empty results list")
    result: Dict = results[0]

    # Get results->geometry->location subdict.
    location_key_path = ["geometry", "location"]
    location: Dict = utils_dictionary.get_nested_value(
        dictionary=result,
        keys=location_key_path,
        default=None,
    )
    if not location:
        raise ValueError("Invalid empty location dict")

    # Get latitude and longitude from location subdict.
    lat = location.get("lat", None)
    lng = location.get("lng", None)
    if not lat or not lng:
        raise ValueError("Unable to parse valid (lat, lng) from location dict")

    # Return corresponding LatLng model instance.
    return LatLng(lat=lat, lng=lng)
