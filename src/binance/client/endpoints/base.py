"""
Endpoint base classes
=====================

- _Parameters
- _Endpoint
- Endpoints
- LinkEndpointsMixin
"""
import inspect
import functools
import logging

from urllib.parse import urlencode
from pydantic import validate_arguments, BaseModel
from typing import Callable, Type, TypeVar, TYPE_CHECKING, Iterator


from binance.enums import http
from binance.order.base import Order

if TYPE_CHECKING:
    from binance.client.base import BaseClient

log = logging.getLogger(__name__)


class APIParameters:
    """
    API parameters container and encoder.

    Parameters
    ----------
    params: dict[str, ...]
        Parameters to contain
    """
    __slots__ = ['params']

    def __init__(self, params):
        self.params = dict()
        for key, val in params.items():
            self[key] = val

    def __repr__(self) -> str:
        return f'APIParameters({self.params})'

    def __setitem__(self, key, val):
        if val is not None:
            val = val() if callable(val) else str(val)
            self.params[key] = val

    def __getitem__(self, key):
        return self.params[key]

    def urlencode(self) -> str:
        """
        Url encode parameters.

        Returns
        -------
        str
            Url encoded string of parameters
        """
        return urlencode(self.params)


class APIEndpoint:
    """
    API Endpoint container and wrapper.

    Parameters
    ----------
    http_method: :class:`binance.enums.http.Method`
        HTTP method to use.
    route: str
        Route of endpoint
    headers: dict[str, str]
        Headers to include in API call
    add_api_key: bool
        Boolean indicating whether to add API key
    add_signature: bool
        Boolean indicating whether to add API signature
    """
    __slots__ = [
        'http_method',
        'route',
        'headers',
        'add_api_key',
        'add_signature',
        'func',
        'func_signature'
    ]

    def __init__(self,
                 http_method: http.Method,
                 route: str,
                 func: Callable,
                 /,
                 headers: dict = None,
                 add_api_key: bool = False,
                 add_signature: bool = False):
        self.http_method: http.Method = http.Method(http_method)
        self.route = route
        self.headers = headers
        self.add_api_key = add_api_key
        self.add_signature = add_signature
        self.func = func
        self.func_signature = inspect.signature(self.func)

    def __repr__(self) -> str:
        return f'Endpoint(http_call={self.http_call}, route={self.route}, func={self.func}, headers={self.headers}, api_key={self.api_key}, add_signature={self.sign})'

    def __get_params(self, args, kwargs) -> APIParameters:
        """
        Creates APIParameters object from args and kwargs

        Parameters
        ----------
        args: list
            args to extract parameters from
        kwargs: dict
            kwargs to extract parameters from
        
        Returns
        -------
        :class:`APIParameters`
            APIParameters object with parameters extracted from args and kwargs
        """
        ba = self.func_signature.bind(*args, **kwargs)
        ba.apply_defaults()
        
        # unpack pydantic basemodels into parameters
        for key, param in ba.signature.parameters.items():
            if param.annotation is BaseModel:
                arg = ba.arguments.pop(key)
                ba.arguments.update(arg.dict(exclude_none=True))

        return APIParameters(ba.arguments)

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
                                          params=self.__get_params(args, kwargs),
                                          headers=self.headers,
                                          add_api_key=self.add_api_key,
                                          add_signature=self.add_signature)
        else:
            @validate_arguments(config=dict(arbitrary_types_allowed=True))
            @functools.wraps(self.func)
            def wrapper(*args, **kwargs):
                return client._call(self.http_method,
                                    self.route,
                                    params=self.__get_params(args, kwargs),
                                    headers=self.headers,
                                    add_api_key=self.add_api_key,
                                    add_signature=self.add_signature)
        return wrapper


class APIEndpoints:
    """
    API endpoints container and decorator.
    """
    __slots__ = ['__endpoints']

    def __init__(self):
        self.__endpoints = list()

    def __iter__(self) -> Iterator[APIEndpoint]:
        return iter(self.__endpoints)

    def __repr__(self):
        return f'Endpoints({str(self.__endpoints)})'

    def add(self,
            http_method: http.Method,
            route: str,
            /,
            headers: dict[str, str]=None,
            add_api_key: bool=False,
            add_signature: bool=False):
        """
        Decorator for adding endpoint to container.

        Parameters
        ----------
        http_method: :class:`binance.enums.http.Method`
            HTTP method to use.
        route: str
            Route of endpoint
        headers: dict[str, str]
            Dictionary of headers
        add_api_key: bool
            Boolean indicating whether to add API key
        add_signature: bool
            Boolean indicating whether to add API signature
        
        Returns
        -------
        Callable
            Original callable on which decoratorwas called
        """
        log.debug("adding %s endpoint")
        def decorator(func):
            ep = APIEndpoint(http_method,
                           route,
                           func,
                           headers=headers,
                           add_api_key=add_api_key,
                           add_signature=add_signature)
            self.__endpoints.append(ep)
            return func
        return decorator


APIEndpointsType = TypeVar('APIEndpointsType', bound='APIEndpointsLinkerMixin')

class APIEndpointsLinkerMixin:
    """
    API endpoints linker mixin used to link API endspoints to a binance client.
    """
    endpoints: APIEndpoints

    @classmethod
    def link(cls: Type[APIEndpointsType], client: 'BaseClient') -> APIEndpointsType:
        """
        Links API endpoints to parsed client.

        Parameters
        ----------
        client: :class:`binance.client.base.BaseClient`
            Binance client to link endpoints to
        
        Returns
        -------
        :class:`APIEndpointsType`
            Subclass instance with API endpoints wrapped with parsed binance client
        """
        self = cls()
        for e in cls.endpoints:
            endpoint_name = e.func.__name__
            client_wrapped_endpoint = e.wrap(client)
            self.__setattr__(endpoint_name, client_wrapped_endpoint)
        return self
