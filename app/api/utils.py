"""
API utils.
"""

# External imports
from typing import Any, Dict, List
from flask import jsonify

# Internal imports
# - N/A

# Constants
HTTP_STATUS_OK = 200
HTTP_STATUS_ERR_BAD_REQUEST = 400
HTTP_STATUS_ERR_INTERNAL_SERVER_ERROR = 500


#####################
# SUCCESS RESPONSES #
#####################

def jsonify_success_data(data: Any) -> str:
    """
    Given some data that we want to write back to the client as part of a
    successful request, JSONify the data to a string and return in the expected
    API format.

    In this case, we follow the JSON API (see jsonapi.org) for a basic common
    structure for all request responses. In particular, since this is a
    success response, all we need to do is include the data value under the
    "data" key in a dict, and JSONify that dict to a string.
    """
    return jsonify({"data": data})


###################
# ERROR RESPONSES #
###################

class APIError(object):
    """
    TODO: Document.
    """

    def __init__(self, status: int, title: str) -> None:
        self.status = status
        self.title = title

    def to_dict(self) -> Dict:
        """
        TODO: Document.
        """
        return {
            "status": self.status,
            "title": self.title,
        }


def jsonify_error_data(errors: List[APIError]) -> str:
    """
    Given a list of APIError instances, place them under the "errors" key in a
    dict, and JSONify the dict to an output string.
    """
    return jsonify({
        "errors": [api_error.to_dict() for api_error in errors],
    })
