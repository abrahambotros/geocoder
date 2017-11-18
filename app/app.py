"""
Entry-point for this application.
"""

# External modules
from flask import Flask, jsonify

# Internal modules
from app.controllers import main as main_controller


# Instantiate the Flask app server, once and for all.
SERVER = Flask(__name__)


@SERVER.route("/", methods=["GET"])
def geocode() -> str:
    """
    Root geocode response handler.

    TODO: Parse address from request.
    TODO: Handle errors.
    """
    # Parse address from request.
    # TODO: Implement.

    # Pass address from request to main geocoding controller to get geocoded
    # LatLng response.
    try:
        lat_lng = main_controller.geocode(
            address="",
        )
    except Exception:
        return jsonify({})

    # TODO: Handle errors from geocoding functions.

    # JSON-ify the LatLng data and respond to client.
    return jsonify(lat_lng.to_dict())
