"""
Entry-point for this application.
"""

# External modules
from flask import Flask, jsonify, request

# Internal modules
from app.controllers import main as main_controller

# Constants
_URL_PARAM_ADDRESS = "address"

# Instantiate the Flask app server, once and for all.
SERVER = Flask(__name__)


@SERVER.route("/", methods=["GET"])
def geocode() -> str:
    """
    Root geocode response handler.

    TODO: Handle errors.
    """
    # Parse address from request.
    address = request.args.get(_URL_PARAM_ADDRESS)

    # Pass address from request to main geocoding controller to get geocoded
    # LatLng response.
    try:
        lat_lng = main_controller.geocode(address=address)
    except Exception:
        return jsonify({})

    # TODO: Handle errors from geocoding functions.

    # JSON-ify the LatLng data and respond to client.
    return jsonify(lat_lng.to_dict())
