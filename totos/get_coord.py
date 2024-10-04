import requests
"""
This module will get distances from the BAN API"
"""
def get_coordinates(address: str) -> list:
    """
    This function takes an address as input and returns
    a list of coordinates.
    """
    URL = "https://api-adresse.data.gouv.fr/search/?q="
    r = requests.get(URL + address)
    return r.json()['features'][0]['geometry']['coordinates'][::-1]