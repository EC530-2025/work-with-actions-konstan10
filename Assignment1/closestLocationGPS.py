from collections import defaultdict
from math import radians, atan2, sin, cos, sqrt
from typing import List

import cProfile
import logging
import tracemalloc

def closestLocationGPS(arr1: List[tuple], arr2: List[tuple]) -> dict:
    """
    This function takes two geo-location arrays and finds the points from the 2nd array that are closest to the points in the 1st array,
    and puts the pairs into a dictionary.

    Args: 
        arr1 (List[tuple]): base array
        arr2 (List[tuple]): array for comparison
    
    Returns:
        dict: dictionary of results, keys are from arr2 and values are from arr1
    """
    try:
        assert isinstance(arr1, List) and isinstance(arr2, List), "Input needs to be a list/array type"
        assert len(arr1) > 0 and len(arr2) > 0, "Neither of the arrays should be empty"
        assert all(isinstance(pair1, tuple) for pair1 in arr1) and all(isinstance(pair2, tuple) for pair2 in arr2), "Arrays should have tuples"

        for arr1_pair, arr2_pair in zip(arr1, arr2):
            assert len(arr1_pair) == 2 and len(arr2_pair) == 2, "Arrays should contain only two coordinates"
            lat1, lon1 = arr1_pair
            lat2, lon2 = arr2_pair
            assert isinstance(lat1, float) or isinstance(lat1, int), "Coordinates must be integers or floats"
            assert isinstance(lat2, float) or isinstance(lat2, int), "Coordinates must be integers or floats"
            assert isinstance(lon1, float) or isinstance(lon1, int), "Coordinates must be integers or floats"
            assert isinstance(lon2, float) or isinstance(lon2, int), "Coordinates must be integers or floats"
            assert abs(lat1) <= 90 and abs(lat2) <= 90, "Absolute value of latitude should be <= 90"
            assert abs(lon1) <= 180 and abs(lon2) <= 180, "Absolute value of longitude should be <= 180"

        closest_location_map = defaultdict(list)
        for arr1_pair in arr1:
            lat1, lon1 = arr1_pair
            closest_distance = None
            closest_pair = None
            for arr2_pair in arr2:
                lat2, lon2 = arr2_pair

                # Formula for calculating distance
                diff_lat = radians(lat2 - lat1)
                diff_lon = radians(lon2 - lon1)

                res = sin(diff_lat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(diff_lon / 2) ** 2
                res = atan2(sqrt(res), sqrt(1 - res))

                # Compare and update closest values
                if closest_distance is None:
                    closest_distance = res
                    closest_pair = arr2_pair
                else:
                    temp_distance = closest_distance
                    closest_distance = min(closest_distance, res)
                    if temp_distance != closest_distance:
                        closest_pair = arr2_pair     

            closest_location_map[closest_pair].append(arr1_pair)
        
        return dict(closest_location_map)
    except AssertionError as e:
        print(f"Assertion Error occured: {e}")
        return {}

if __name__ == "__main__":
    tracemalloc.start()
    logging.basicConfig(level = logging.INFO)

    logger = logging.getLogger(__name__)
    arr1 = [(-68.53306, -108.09832), (37.7749, -122.4194), (79.75216, 97.65512)]
    arr2 = [(-5.62852, -144.59028), (34.052235, -118.243683)]
    
    result = closestLocationGPS(arr1, arr2)
    cProfile.run('closestLocationGPS(arr1, arr2)')
    logger.info(result)

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    logger.info("[ Top 10 ]")
    for stat in top_stats[:10]:
        logger.info(stat)  