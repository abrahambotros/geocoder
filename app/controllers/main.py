"""
Main controller providing a simple interface for API requests to geocode based
on an input address string. Abstracts away callers from having to interact with
third-party geocoding service requests and backup/fallback logic.
"""

# External imports
import logging

# Internal imports
from app.controllers.third_party import google_maps as gmaps_controller, here as here_controller
from app.models.lat_lng import LatLng


def geocode(address: str) -> LatLng:
    """Geocode the given address string to (lat, lng) coordinates, by making a
    manual HTTP request to one of the third-party geocoding service APIs
    supported by this package. Currently, this is either the Google Maps
    Geocoding API, or the HERE Geocoder API.

    If there is an error in any request to/parsing of a third-party geocoding
    API, then fall back to other APIs, if possible. Currently, this first
    attempts to geocode via the Google Maps Geocoding API, and falls back to the
    HERE Geocoder API otherwise. If all APIs are exhausted with no success, then
    an error is thrown as indicated below.

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

    # Make geocode requests, with ordered list of geocode functions to try
    # (along with a short description indicating the geocoding service being
    # used for logging).
    #
    # The first is the primary request function, the second is the fallback if
    # the primary fails, etc. Assumes geocode functions all have the same form
    # of `geocode(address=<str>)`, and raise a RuntimeError on any errors.
    for geocode_fn, service_description in [
            (gmaps_controller.geocode, "Google Maps Geocoding API"),
            (here_controller.geocode, "HERE Geocoder API")]:
        try:
            return geocode_fn(address=address)
        except RuntimeError:
            logging.warning(
                "Error geocoding via %s; " +
                "falling back to next available service",
                service_description,
            )

    # If reach here, then all geocoding requests have failed, and we should
    # instead raise an exception.
    raise RuntimeError("Unable to geocode requested address")
