"""
Provides the simple LatLng model used throughout the rest of the app. Provides
some useful utilities for comparing coordinate pairs too.
"""

# External imports
# - N/A

# Internal imports
# - N/A


class LatLng(object):
    """
    Simple model for representing a (latitude, longitude) numeric 2-tuple.
    """

    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng
