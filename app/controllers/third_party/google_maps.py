"""
Controller file implementing geocoding requests to the Google Maps Geocoding
API.
"""

# External imports
from typing import Dict

# Internal imports
from app.models.lat_lng import LatLng
from app.conf.settings import GMAPS_API_KEY
from app.controllers.third_party.request import make_geocode_request
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

    # Make geocode request to Google Maps Geocoding API. Get result as JSON
    # dict.
    resp_dict = make_geocode_request(
        base_url=_URL_GEOCODE_BASE,
        params_dict=params_dict,
    )

    # Parse response data dict's latitude and longitude into LatLng instance and
    # return with success. If error, raise exception.
    try:
        return _parse_geocode_response_dict_to_lat_lng(resp_dict)
    except Exception:
        raise RuntimeError("Error parsing Google Maps Geocoding API response")


def _parse_geocode_response_dict_to_lat_lng(resp_dict: Dict) -> LatLng:
    """
    TODO: Document. Raises exception.
    """
    # If invalid input, raise error.
    if not resp_dict:
        raise ValueError("Invalid empty input dict")

    # Get top-level result from results list.
    results = resp_dict["results"]
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
