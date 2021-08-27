#!/usr/bin/env python3
import json
import inspect
import functools

from urllib.parse import urlencode

from binance.enums import http


class _Parameters():
    """
    Class for containing a API parameters and encoding them
    """
    __slot__ = ['__params']
    def __init__(self, params):
        self.__params = dict()
        if params is not None:
            for key, value in params.items():
                self[key] = value
    
    def __repr__(self):
        return f'Parameters({self.__params})'

    def __setitem__(self, key, val):
        if val is not None:
            self.__params[key] = str(val)

    def __getitem__(self, key):
        return self.__params[key]

    def urlencode(self):
        """
        Url encodes parameters

        Returns
        str
            Url encoded string of parameters
        """
        params = dict()
        for key, val in self.__params.items():
            if isinstance(val, list):
                params[key] = json.dumps(val)
            elif isinstance(val, float):
                params[key] = (f'{val:.20f}')[slice(0, 16)].rstrip('0').rstrip('.')
            else:
                params[key] = str(val)
        return urlencode(params)


class _Endpoint():
    """
    Class for containing a API endpoint
    """
    __slots__ = ['http_call', 'route', 'headers', 'api_key', 'sign', 'func']

    def __init__(self, http_call: http.Call, route: str, func: object, /,
                 headers: dict = None, api_key: bool = False, sign: bool = False):
        self.http_call = http_call
        self.route = route
        self.headers = headers
        self.api_key = api_key
        self.sign = sign
        self.func = func
    
    def __repr__(self):
        return f'Endpoint(http_call={self.http_call}, route={self.route}, func={self.func}, headers={self.headers}, api_key={self.api_key}, sign={self.sign})'
    
    def wrap(self, client):
        """
        Wraps API endpoint with client.

        Parameters
        ----------
        client : binance.Client
            Binance client instance
        
        Returns
        -------
        coroutine
            Coroutine which prepares params and uses client to make a http call.
        """
        func_signature = inspect.signature(self.func)
        @functools.wraps(self.func)
        async def wrapper(*args, **kwargs):
            ba = func_signature.bind(*args, **kwargs)
            ba.apply_defaults()
            params = ba.arguments if ba is not None else None
            params = _Parameters(params)
            return await client._call(self.http_call, self.route,  params=params, headers=self.headers, api_key=self.api_key, sign=self.sign)
        return wrapper


class Endpoints():
    """
    Class for containing and decorating API endpoints.
    """
    def __init__(self, name):
        self.name = name
        self.__endpoints = list()

    def __repr__(self):
        return f'Endpoints({str(self.__endpoints)})'

    def get(self, route, /, headers:dict=None, api_key:bool=False, sign:bool=False):
        """
        GET http request decorator.

        Parameters
        ----------
        route : str
            Route of API endpoint
        headers : dict, optional
            Headers to add to http request
        api_key : bool, default=False
            Whether or not to include API key in header
        sign : bool, default=False
            Whether or not to add signature to params
        """
        http_call = http.Call.GET
        def decorator(func):
            endpoint = _Endpoint(http_call, route, func, headers=headers, api_key=api_key, sign=sign)
            self.__endpoints.append(endpoint)
        return decorator
    
    def post(self, route, /, headers=None, api_key=False, sign=False):
        """
        POST http request decorator.

        Parameters
        ----------
        route : str
            Route of API endpoint
        headers : dict, optional
            Headers to add to http request
        api_key : bool, default=False
            Whether or not to include API key in header
        sign : bool, default=False
            Whether or not to add signature to params
        """
        http_call = http.Call.POST
        def decorator(func):
            endpoint = _Endpoint(http_call, route, func, headers=headers, api_key=api_key, sign=sign)
            self.__endpoints.append(endpoint)
        return decorator
    
    @property
    def list(self):
        return self.__endpoints
