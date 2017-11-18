"""
Controller file implementing geocoding requests to the here Geocoder API.
"""

# External imports
from json import JSONDecodeError
from typing import Dict, List, Union
from urllib.error import URLError

# Internal imports
from app.conf.settings import HERE_APP_ID, HERE_APP_CODE
from app.controllers.third_party.request import make_geocode_request
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

    Args:
        address: String representing the address we want to geocode.

    Returns:
        LatLng containing the latitude and longitude corresponding to the
            address that was geocoded.

    Raises:
        RuntimeError: If any errors while geocoding the given address to a valid
            LatLng instance.
    """
    # If invalid address (empty, not string, empty string, or anything otherwise
    # falsy), then raise exception now.
    if not address or not isinstance(address, str):
        raise RuntimeError("Invalid/empty address")

    # Build URL params dict for request, with address string and HERE keys from
    # settings.
    params_dict: Dict[str, str] = {
        _URL_PARAM_ADDRESS: address,
        _URL_PARAM_APP_ID: HERE_APP_ID,
        _URL_PARAM_APP_CODE: HERE_APP_CODE,
    }

    # Make geocode request to HERE Geocoder API. Get result as JSON dict.
    try:
        resp_dict = make_geocode_request(
            base_url=_URL_GEOCODE_BASE,
            params_dict=params_dict,
        )
    except URLError:
        raise RuntimeError("Error making request to HERE Geocoder API")
    except JSONDecodeError:
        raise RuntimeError(
            "Error parsing JSON response from HERE Geocoder API",
        )

    # Parse response data dict's latitude and longitude into LatLng instance and
    # return with success. If error, raise exception.
    try:
        return _parse_geocode_response_dict_to_lat_lng(resp_dict)
    except Exception:
        raise RuntimeError("Error parsing HERE Geocoder API response")


def _parse_geocode_response_dict_to_lat_lng(resp_dict: Dict) -> LatLng:
    """Parse the given response dictionary from the HERE Geocoder API to
    a valid LatLng instance.

    Args:
        resp_dict: Dictionary of the form given by responses from the HERE
            Geocoder API.

    Returns:
        LatLng containing the latitude and longitude corresponding to the
            address that was geocoded.

    Raises:
        RuntimeError: If any errors while geocoding the given address to a valid
            LatLng instance.
    """
    # If invalid input, raise error.
    if not resp_dict:
        raise ValueError("Invalid empty input dict")

    # Get Response->View sublist.
    view: Union[List, None] = utils_dictionary.get_nested_value(
        dictionary=resp_dict,
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
