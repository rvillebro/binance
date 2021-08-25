#!/usr/bin/env python3
import inspect
import functools

from binance.parameters import Parameters
from binance.enums import http

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
        return f'ep(http_call={self.http_call}, route={self.route}, func={self.func}, headers={self.headers}, api_key={self.api_key}, sign={self.sign})'
    
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
            params = Parameters(params)
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
        http_call = http.Call.POST
        def decorator(func):
            endpoint = _Endpoint(http_call, route, func, headers=headers, api_key=api_key, sign=sign)
            self.__endpoints.append(endpoint)
        return decorator
    
    @property
    def list(self):
        return self.__endpoints
