"""
Entry-point for this application.
"""

# External modules
from flask import Flask

# Internal modules
from app.controllers import main as main_controller


# Instantiate the Flask app, once and for all.
APP = Flask(__name__)


@APP.route("/", methods=["GET"])
def geocode() -> str:
    """
    Root geocode response handler.

    TODO: Adjust return type.
    """
    # Parse address from request.
    # TODO: Implement.

    # Pass address from request to main geocoding controller to get geocoded
    # response.
    data = main_controller.geocode(
        address="",
    )

    # TODO: Handle errors from geocoding functions.

    # TODO: Perform any JSON serialization appropriate for the geocoding data
    #    before responding to client.

    return data
