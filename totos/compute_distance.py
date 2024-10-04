from haversine import haversine
"""
This module will compute distances.
"""
def compute_distance(first_place: str, second_place: str) -> float:
    """
    Takes two addresses and returns a distance in kms (float).
    """
    return haversine(first_place, second_place)