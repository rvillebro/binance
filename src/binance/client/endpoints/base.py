"""
Endpoint base classes
=====================

- _Parameters
- _Endpoint
- Endpoints
"""
from __future__ import annotations
import inspect
import functools

from pydantic import validate_arguments
from urllib.parse import urlencode
from typing import TYPE_CHECKING

from binance.enums import http
from binance.order.base import Order
from binance.client.response import Response


class _Parameters:
    """
    Class for containing API parameters and encoding them.
    """
    __slot__ = ['params']

    def __init__(self, params):
        self.params = dict()
        for key, val in params.items():
            self[key] = val

    def __repr__(self):
        return f'Parameters({self.params})'

    def __setitem__(self, key, val):
        if val is not None:
            val = val() if callable(val) else str(val)
            self.params[key] = val

    def __getitem__(self, key):
        return self.params[key]

    def urlencode(self):
        """
        Url encodes parameters.

        Returns
        str
            Url encoded string of parameters
        """
        return urlencode(self.params)


class _Endpoint:
    """
    Class for containing an API endpoint.
    """
    __slots__ = [
        'http_method', 'route', 'headers', 'add_api_key', 'add_signature',
        'func', 'func_sig'
    ]

    def __init__(self,
                 http_method: http.Method,
                 route: str,
                 func: object,
                 /,
                 headers: dict = None,
                 add_api_key: bool = False,
                 add_signature: bool = False):
        self.http_method = http.Method(http_method)
        self.route = route
        self.headers = headers
        self.add_api_key = add_api_key
        self.add_signature = add_signature
        self.func = func
        self.func_sig = inspect.signature(self.func)

    def __repr__(self):
        return f'Endpoint(http_call={self.http_call}, route={self.route}, func={self.func}, headers={self.headers}, api_key={self.api_key}, add_signature={self.sign})'

    @staticmethod
    def unpack_orders(arguments, parameters):
        kwargs = dict(exclude_none=True)
        for key, param in parameters.items():
            if param.annotation == Order:
                arg = arguments.pop(key)
                arguments.update(arg.dict(**kwargs))
            elif param.annotation == list[Order]:
                arguments[key] = [o.dict() for o in val]

    def _get_params(self, args, kwargs):
        ba = self.func_sig.bind(*args, **kwargs)
        ba.apply_defaults()

        self.unpack_orders(ba.arguments, self.func_sig.parameters)

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
            @validate_arguments(config=dict(arbitrary_types_allowed=True))
            @functools.wraps(self.func)
            async def wrapper(*args, **kwargs):
                return await client._call(self.http_method,
                                          self.route,
                                          params=self._get_params(args, kwargs),
                                          headers=self.headers,
                                          add_api_key=self.add_api_key,
                                          add_signature=self.add_signature)
        else:
            @validate_arguments(config=dict(arbitrary_types_allowed=True))
            @functools.wraps(self.func)
            def wrapper(*args, **kwargs):
                return client._call(self.http_method,
                                    self.route,
                                    params=self._get_params(args, kwargs),
                                    headers=self.headers,
                                    add_api_key=self.add_api_key,
                                    add_signature=self.add_signature)

        return wrapper


class Endpoints:
    """
    Class for containing API endpoints.
    """
    __endpoints = list()

    def __repr__(self):
        return f'Endpoints({str(self.__endpoints)})'

    @classmethod
    def add(cls,
            http_method,
            route,
            /,
            headers=None,
            add_api_key=False,
            add_signature=False):

        def decorator(func):
            ep = _Endpoint(http_method,
                           route,
                           func,
                           headers=headers,
                           add_api_key=add_api_key,
                           add_signature=add_signature)
            cls.__endpoints.append(ep)
            return func

        return decorator

    def __iter__(self):
        return iter(self.__endpoints)


class LinkEndpointsMixin:
    """
    Mixin used to add link API endspoints method.
    """

    @classmethod
    def link(cls, client: 'BaseClient'):
        """
        Links endpoints to parsed client.

        Parameters
        ----------
        client : BaseClient
            client to link endpoints to
        """
        self = cls()
        for e in cls.endpoints:
            endpoint_name = e.func.__name__
            client_wrapped_endpoint = e.wrap(client)
            self.__setattr__(endpoint_name, client_wrapped_endpoint)
        return self
