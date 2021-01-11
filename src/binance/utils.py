#!/usr/bin/env python3.8
import time

def clean_params(params):
    """
    Removes all key-value pairs have a value of None

    Args:
        params (dict): parameter dictionary to clean
    
    Return:
        dict: cleaned parameters dictionary
    """
    cleaned_params = dict()
    for key, value in params.items():
        if value is not None:
            cleaned_params[key] = str(value)
    
    return cleaned_params


def get_timestamp():
    """
    Gets timestamp in miliseconds

    Return:
        int: timestamp in miliseconds
    """
    timestamp = int(round(time.time() * 1000))
    return timestamp
