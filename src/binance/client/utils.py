#!/usr/bin/env python3.8
import time

def clean_params(params):
    cleaned_params = dict()
    for key, value in params.items():
        if value is not None:
            cleaned_params[key] = str(value)
    
    return cleaned_params


def get_timestamp():
    timestamp = int(round(time.time() * 1000))
    return timestamp
