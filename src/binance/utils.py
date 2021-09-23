#!/usr/bin/env python3
import time

def get_timestamp():
    """
    Gets timestamp in miliseconds

    Return:
        int: timestamp in miliseconds
    """
    timestamp = int(round(time.time() * 1000) - 10000)
    return timestamp