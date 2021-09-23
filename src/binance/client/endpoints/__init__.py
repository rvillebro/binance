#!/usr/bin/env python3
import json
import inspect
import functools

from urllib.parse import urlencode

from binance.enums import http


class _Parameters():
    """Class for containing API parameters and encoding them."""
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
        Url encodes parameters.

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
    """Class for containing an API endpoint."""
    __slots__ = ['http_method', 'route', 'headers', 'add_api_key', 'add_signature', 'func', 'func_signature']

    def __init__(self, http_method: http.Method, route: str, func: object, /,
                 headers: dict = None, add_api_key: bool = False, add_signature: bool = False):
        self.http_method = http.Method(http_method)
        self.route = route
        self.headers = headers
        self.add_api_key = add_api_key
        self.add_signature = add_signature
        self.func = func
        self.func_signature = inspect.signature(func)

    def __repr__(self):
        return f'Endpoint(http_call={self.http_call}, route={self.route}, func={self.func}, headers={self.headers}, api_key={self.api_key}, sign={self.sign})'
    
    def _get_params(self, args, kwargs):
        ba = self.func_signature.bind(*args, **kwargs)
        ba.apply_defaults()
        params = ba.arguments if ba is not None else None
        params = _Parameters(params)
        return params
   
    def wrap(self, client, /, asynchronous=True):
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
        if asynchronous:
            @functools.wraps(self.func)
            async def wrapper(*args, **kwargs):
                return await client._call(
                    self.http_method,
                    self.route,
                    params=self._get_params(args, kwargs),
                    headers=self.headers,
                    add_api_key=self.add_api_key,
                    add_signature=self.add_signature
                )
        else:
            @functools.wraps(self.func)
            def wrapper(*args, **kwargs):
                return client._call(
                    self.http_method,
                    self.route,
                    params=self._get_params(args, kwargs),
                    headers=self.headers,
                    add_api_key=self.add_api_key,
                    add_signature=self.add_signature
                )

        return wrapper


class Endpoints():
    """Class for containing and decorating API endpoints."""
    def __init__(self, name):
        self.name = name
        self.__endpoints = list()

    def __repr__(self):
        return f'Endpoints({str(self.__endpoints)})'
    
    def add(self, http_method, route, /, headers=None, add_api_key=False, add_signature=False):
        def decorator(func):
            endpoint = _Endpoint(
                http_method,
                route,
                func,
                headers=headers,
                add_api_key=add_api_key,
                add_signature=add_signature
            )
            self.__endpoints.append(endpoint)
        return decorator
    
    def to_list(self):
        return self.__endpoints