"""
Entry-point for this application.
"""

# External modules
from flask import Flask

# Internal modules
# - N/A


# Instantiate the Flask app, once and for all.
APP = Flask(__name__)


@APP.route("/", methods=["GET"])
def root() -> str:
    """
    Placeholder root responder.
    """
    return "I am alive!"
