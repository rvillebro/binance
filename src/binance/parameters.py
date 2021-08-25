#!/usr/bin/env python3
import json

from urllib.parse import urlencode

class Parameters():
    __slot__ = ['__params']
    def __init__(self, params):
        self.__params = dict()
        if params is not None:
            for key, value in params.items():
                self[key] = value
    
    def __setitem__(self, key, val):
        if val is not None:
            self.__params[key] = str(val)

    def __getitem__(self, key):
        return self.__params[key]

    def __repr__(self):
        return f'Parameters({self.__params})'

    def urlencode(self):
        params = dict()
        for key, val in self.__params.items():
            if isinstance(val, list):
                params[key] = json.dumps(val)
            elif isinstance(val, float):
                params[key] = (f'{val:.20f}')[slice(0, 16)].rstrip('0').rstrip('.')
            else:
                params[key] = str(val)
        return urlencode(params)
