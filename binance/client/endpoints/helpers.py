"""
"""
import time


def get_timestamp():
    """
    Gets timestamp in miliseconds

    Return:
        int: timestamp in miliseconds
    """
    timestamp = int(round(time.time() * 1000))
    return timestamp
