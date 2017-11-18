"""
Utils for controller tests.
"""

# External imports
from typing import Dict

# Internal imports
from app.models.lat_lng import LatLng


ADDRESS_TO_LATLNG_DICT: Dict[str, LatLng] = {
    "1600 Amphitheatre Parkway, Mountain View, CA": LatLng(lat=37.422408, lng=-122.085609),
    "San Francisco, CA, USA": LatLng(lat=37.77493, lng=-122.419416),
    "san francisco": LatLng(lat=37.77493, lng=-122.419416),
    "1600 Pennsylvania Ave NW, Washington, DC 20500": LatLng(lat=38.897663, lng=-77.036574),
    "colossus of rhodes": LatLng(lat=36.451066, lng=28.225833),
    "Great Pyramid of Giza": LatLng(lat=29.979235, lng=31.134202),
    "hanging gardens of babylon": LatLng(lat=48.919861, lng=2.343222),
}
