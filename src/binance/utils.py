#!/usr/bin/env python3.8
import time
import json

def get_timestamp():
    """
    Gets timestamp in miliseconds

    Return:
        int: timestamp in miliseconds
    """
    timestamp = int(round(time.time() * 1000) - 10000)
    return timestamp


class EnumStringMixin():
    def __str__(self):
        return self.value