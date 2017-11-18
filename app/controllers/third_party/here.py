"""
Controller file implementing geocoding requests to the here Geocoder API.
"""

# External imports
import json
import ssl
import urllib.request
from urllib.parse import urlencode
from typing import Dict, List, Union

# Internal imports
from app.conf.settings import HERE_APP_ID, HERE_APP_CODE
from app.models.lat_lng import LatLng
from app.utils import dictionary as utils_dictionary

# Constants
_URL_GEOCODE_BASE = "https://geocoder.cit.api.here.com/6.2/geocode.json"
_URL_PARAM_ADDRESS = "searchtext"
_URL_PARAM_APP_ID = "app_id"
_URL_PARAM_APP_CODE = "app_code"


def geocode(address: str) -> LatLng:
    """
    Geocode the given address string to (lat, lng) coordinates, by making a
    manual HTTP request to the here Geocoder API.
    """
    # Build URL params dict for request, with address string and HERE keys from
    # settings.
    params_dict: Dict[str, str] = {
        _URL_PARAM_ADDRESS: address,
        _URL_PARAM_APP_ID: HERE_APP_ID,
        _URL_PARAM_APP_CODE: HERE_APP_CODE,
    }

    # URL-encode the URL params dict into a URL-encoded string.
    params_str: str = urlencode(params_dict)

    # Fire off the request to the HERE Geocoder API. Parse response to JSON
    # dict.
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
        raise RuntimeError("Error parsing HERE Geocoder API response")


def _parse_geocode_response_dict_to_lat_lng(d: Dict) -> LatLng:
    """
    TODO: Document. Raises exception.
    TODO: Implement.
    """
    # If invalid input, raise error.
    if not d:
        raise ValueError("Invalid empty input dict")

    # Get Response->View sublist.
    view: Union[List, None] = utils_dictionary.get_nested_value(
        dictionary=d,
        keys=["Response", "View"],
        default=None,
    )
    if not view:
        raise ValueError("Invalid empty view list")
    # Get first element in View list.
    top_view: Dict = view[0]

    # Get Response->View->Result sublist.
    result: Union[List, None] = top_view.get("Result", None)
    if not result:
        raise ValueError("Invalid empty result list")
    # Get first element in Result list.
    top_result = result[0]

    # Get Response->View->Result->Location->DisplayPosition subdict.
    display_position = utils_dictionary.get_nested_value(
        dictionary=top_result,
        keys=["Location", "DisplayPosition"],
        default=None
    )
    if not display_position:
        raise ValueError("Invalid empty DisplayPosition dict")

    # Get latitude and longitude from DisplayPosition subdict.
    lat = display_position.get("Latitude", None)
    lng = display_position.get("Longitude", None)
    if not lat or not lng:
        raise ValueError(
            "Unable to parse valid (lat, lng) from DisplayPosition dict")

    # Return corresponding LatLng model instance.
    return LatLng(lat=lat, lng=lng)
