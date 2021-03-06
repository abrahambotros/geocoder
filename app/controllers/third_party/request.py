"""
Shared request logic for third-party geocoding requests.
"""

# External imports
import json
import ssl
import urllib.request
from urllib.parse import urlencode
from typing import Dict

# Internal imports
# - N/A


def make_geocode_request(base_url: str, params_dict: Dict[str, str]) -> Dict:
    """
    Given information about a third-party geocoding request to fire off, build
    the request now, send it, and parse the response to JSON before returning.

    Args:
        base_url: String indicating the base URL of the target third-party API
            endpoint.
        params_dict: Dictionary of URL parameters (keys and values) that should
            be encoded into the URL we will send the request to.

    Returns:
        Dictionary representing the JSON response from the third-party geocoding
            API service.

    Raises:
        urllib.error.URLError: If error issuing request to external endpoint.
        json.JSONDecodeError: If error decoding the response string to a JSON
            object.
    """
    # URL-encode the URL params dict into a URL-encoded string.
    params_str: str = urlencode(params_dict)

    # Fire off the request to the base URL, with URL params attached. Parse
    # response to JSON dict. Raised exceptions noted in docstring above.
    url = "%s?%s" % (base_url, params_str)
    # TODO: Python 3's increased SSL security for requests will likely cause a
    #    CERTIFICATE_VERIFY_FAILED error on most local systems without elaborate
    #    certificate setup. Because of this, we currently disable SSL
    #    verification of the CONTROLLED requests we make to the known API
    #    endpoints via the explicit context setting below.
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url=url, context=context) as resp:
        return json.loads(resp.read().decode("utf-8"))
