"""
Endpoint base classes
=====================

- _Parameters
- _Endpoint
- Endpoints
"""
import abc
import json
import inspect
import functools

from pydantic import validate_arguments
from urllib.parse import urlencode

from binance.enums import http

class _Parameters:
    """Class for containing API parameters and encoding them."""
    __slot__ = ['params']

    def __init__(self, params):
        self.params = dict()
        for key, val in params.items():
            self[key] = val
 
    def __repr__(self):
        return f'Parameters({self.params})'
    
    def __setitem__(self, key, val):
        if val is not None:
            self.params[key] = self._encode(val)
    
    def __getitem__(self, key):
        return self.params[key]

    def _encode(self, val):
        if isinstance(val, list):
            val = json.dumps(val)
        elif isinstance(val, float):
            val = (f'{val:.20f}')[slice(0, 16)].rstrip('0').rstrip('.')
        elif callable(val):
            val = val()
        
        return str(val)

    def urlencode(self):
        """
        Url encodes parameters.

        Returns
        str
            Url encoded string of parameters
        """
        return urlencode(self.params)


class _Endpoint:
    """Class for containing an API endpoint."""
    __slots__ = ['http_method', 'route', 'headers', 'add_api_key', 'add_signature', 'func', 'func_sig']

    def __init__(self, http_method: http.Method, route: str, func: object, /,
                 headers: dict = None, add_api_key: bool = False, add_signature: bool = False):
        self.http_method = http.Method(http_method)
        self.route = route
        self.headers = headers
        self.add_api_key = add_api_key
        self.add_signature = add_signature
        self.func = func
        self.func_sig = inspect.signature(self.func)

    def __repr__(self):
        return f'Endpoint(http_call={self.http_call}, route={self.route}, func={self.func}, headers={self.headers}, api_key={self.api_key}, sign={self.sign})'

    def _get_params(self, args, kwargs):
        ba = self.func_sig.bind(*args, **kwargs)
        ba.apply_defaults()

        params = _Parameters(ba.arguments)
        return params

    def wrap(self, client, /):
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
        if client.ASYNCHRONOUS:
            @validate_arguments  # validates the type of parsed arguments
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
            @validate_arguments  # validates the type of parsed arguments
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


class Endpoints(abc.ABC):
    """
    Abstract Class for containing and decorating API endpoints.
    """
    __endpoints = list()

    def __init__(self, client):
        """
        """
        for e in self.__endpoints:
            endpoint_name = e.func.__name__
            client_wrapped_endpoint = e.wrap(client)
            self.__setattr__(endpoint_name, client_wrapped_endpoint)

    def __repr__(self):
        return f'Endpoints({str(self.__endpoints)})'
    
    @classmethod
    def add(cls, http_method, route, /, headers=None, add_api_key=False, add_signature=False):
        def decorator(func):
            ep = _Endpoint(
                http_method,
                route,
                func,
                headers=headers,
                add_api_key=add_api_key,
                add_signature=add_signature
            )
            cls.__endpoints.append(ep)
            return func
        return decorator
    
    def __iter__(self):
        return iter(self.__endpoints)
