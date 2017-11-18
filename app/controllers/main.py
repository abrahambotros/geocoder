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
    """
    Geocode the given address string to (lat, lng) coordinates.

    TODO: Document. Note throws exception.
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
        (here_controller.geocode, "HERE Geocoder API"),
    ]:
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
