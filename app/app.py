"""
Entry-point for this application.
"""

# External modules
from flask import Flask, request

# Internal modules
from app.api import utils as api_utils
from app.controllers import main as main_controller

# Constants
_URL_PARAM_ADDRESS = "address"

# Instantiate the Flask app server, once and for all.
SERVER = Flask(__name__)


@SERVER.route("/", methods=["GET"])
def geocode() -> str:
    """
    Root geocode response handler.
    """
    # Parse address from request.
    address = request.args.get(_URL_PARAM_ADDRESS)
    # If address is empty string, then return error now.
    if not address:
        api_error = api_utils.APIError(
            status=api_utils.HTTP_STATUS_ERR_BAD_REQUEST,
            title="Missing/invalid address parameter",
        )
        return api_utils.jsonify_error_data([api_error])

    # Pass address from request to main geocoding controller to get geocoded
    # LatLng response.
    try:
        lat_lng = main_controller.geocode(address=address)
    except RuntimeError as error:
        # If any errors, then create APIError and respond.
        api_error = api_utils.APIError(
            status=api_utils.HTTP_STATUS_ERR_INTERNAL_SERVER_ERROR,
            title=str(error),
        )
        return api_utils.jsonify_error_data([api_error])

    # JSON-ify the LatLng data and respond to client.
    return api_utils.jsonify_success_data(lat_lng.to_dict())
