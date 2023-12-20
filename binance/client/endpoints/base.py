"""
Endpoint base classes
=====================

- Parameters
- Endpoint
- Endpoints
"""
import functools
import inspect
import logging
from collections.abc import Callable, Iterator, MutableMapping
from types import SimpleNamespace
from typing import TYPE_CHECKING
from urllib.parse import urlencode

from pydantic import BaseModel, validate_call

from binance.enums import HTTPMethod

if TYPE_CHECKING:
    from binance.client.base import BaseClient

log = logging.getLogger(__name__)


class Parameters(MutableMapping):
    """
    API parameters container and encoder.

    Parameters
    ----------
    *args

    **kwargs
    """

    __slots__ = ["__store"]

    def __init__(self, *args, **kwargs):
        self.__store = dict()
        self.update(*args, **kwargs)

    def __setitem__(self, key, val):
        if val is not None:
            val = val() if callable(val) else str(val)
            self.__store[key] = val

    def __getitem__(self, key):
        return self.__store[key]

    def __delitem__(self, key):
        del self.__store[key]

    def __iter__(self):
        return iter(self.__store)

    def __len__(self):
        return len(self.__store)

    @classmethod
    def from_signature(cls, signature: inspect.Signature, args: list, kwargs: dict) -> "Parameters":
        """
        Creates Parameters object from args and kwargs

        Parameters
        ----------
        signature:
            Signature of method
        args: list
            args to extract parameters from
        kwargs: dict
            kwargs to extract parameters from

        Returns
        -------
        :class:`Parameters`
            Parameters object with parameters extracted from args and kwargs
        """
        ba = signature.bind(*args, **kwargs)
        ba.apply_defaults()
        for key in list(ba.arguments.keys()):
            if not isinstance(ba.arguments[key], BaseModel):
                continue
            # unpack pydantic basemodels into parameters
            model: BaseModel = ba.arguments.pop(key)
            model_args = model.model_dump(exclude_none=True)
            ba.arguments.update(model_args)
        return cls(**ba.arguments)

    def urlencode(self) -> str:
        """
        Url encode parameters.

        Returns
        -------
        str
            Url encoded string of parameters
        """
        return urlencode(self.__store)


class Endpoint:
    """
    API Endpoint container and wrapper.

    Parameters
    ----------
    http_method: :class:`binance.enums.HTTPMethod`
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

    __slots__ = ["http_method", "route", "headers", "add_api_key", "add_signature", "func", "func_signature"]

    def __init__(
        self,
        func: Callable,
        http_method: HTTPMethod,
        route: str,
        /,
        headers: dict = None,
        add_api_key: bool = False,
        add_signature: bool = False,
    ):
        self.http_method = HTTPMethod(http_method)
        self.route = route
        self.headers = headers
        self.add_api_key = add_api_key
        self.add_signature = add_signature
        self.func = func
        self.func_signature = inspect.signature(func)

    def __repr__(self) -> str:
        return (
            "Endpoint("
            f"func={self.func}, "
            f"http_method={self.http_method}, "
            f"route={self.route}, "
            f"headers={self.headers}, "
            f"add_api_key={self.add_api_key}, "
            f"add_signature={self.add_signature})"
        )

    def wrap(self, client: "BaseClient"):
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
        endpoint_args = [self.http_method, self.route]
        endpoint_kwargs = dict(headers=self.headers, add_api_key=self.add_api_key, add_signature=self.add_signature)
        if client.ASYNCHRONOUS:

            @functools.wraps(self.func)
            async def wrapper(*args, **kwargs):
                validate_call(config=dict(arbitrary_types_allowed=True))(self.func)
                return await client._call(
                    *endpoint_args,
                    **endpoint_kwargs,
                    params=Parameters.from_signature(self.func_signature, args, kwargs),
                )
        else:

            @functools.wraps(self.func)
            def wrapper(*args, **kwargs):
                return client._call(
                    *endpoint_args,
                    **endpoint_kwargs,
                    params=Parameters.from_signature(self.func_signature, args, kwargs),
                )

        if True:  # client.validate_calls:
            config = dict(arbitrary_types_allowed=True)
            wrapper = validate_call(config=config)(wrapper)
        return wrapper


class Endpoints:
    """
    API endpoints container and decorator.
    """

    __slots__ = ["__endpoints"]

    def __init__(self):
        self.__endpoints: list[Endpoint] = []

    def __iter__(self) -> Iterator[Endpoint]:
        return iter(self.__endpoints)

    def __str__(self):
        return f"<Endpoints: {len(self.__endpoints)}>"

    def __repr__(self):
        return f"Endpoints({self.__endpoints})"

    def add(
        self,
        http_method: HTTPMethod,
        route: str,
        /,
        headers: dict[str, str] = None,
        add_api_key: bool = False,
        add_signature: bool = False,
    ):
        """
        Decorator for adding endpoint to container.

        Parameters
        ----------
        http_method: :class:`binance.enums.HTTPMethod`
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
        log.debug("adding %s at %s", http_method, route)

        def decorator(method: Callable):
            ep = Endpoint(
                method, http_method, route, headers=headers, add_api_key=add_api_key, add_signature=add_signature
            )
            self.__endpoints.append(ep)
            return method

        return decorator

    def get(
        self,
        route: str,
        /,
        headers: dict[str, str] = None,
        add_api_key: bool = False,
        add_signature: bool = False,
    ):
        """
        Adds get endpoint.

        Parameters
        ----------
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
        return self.add(HTTPMethod.GET, route, headers, add_api_key, add_signature)

    def post(
        self,
        route: str,
        /,
        headers: dict[str, str] = None,
        add_api_key: bool = False,
        add_signature: bool = False,
    ):
        """
        Adds post endpoint.

        Parameters
        ----------
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
        return self.add(HTTPMethod.POST, route, headers, add_api_key, add_signature)

    def put(
        self,
        route: str,
        /,
        headers: dict[str, str] = None,
        add_api_key: bool = False,
        add_signature: bool = False,
    ):
        """
        Adds put endpoint.

        Parameters
        ----------
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
        return self.add(HTTPMethod.PUT, route, headers, add_api_key, add_signature)

    def delete(
        self,
        route: str,
        /,
        headers: dict[str, str] = None,
        add_api_key: bool = False,
        add_signature: bool = False,
    ):
        """
        Adds delete endpoint.

        Parameters
        ----------
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
        return self.add(HTTPMethod.DELETE, route, headers, add_api_key, add_signature)

    def link(self, client: "BaseClient"):
        """
        Links API endpoints to parsed client.

        Parameters
        ----------
        client: :class:`binance.client.base.BaseClient`
            Binance client to link endpoints to

        Returns
        -------
        :class:`EndpointsType`
            Subclass instance with API endpoints wrapped with parsed binance client
        """
        return SimpleNamespace(**{e.func.__name__: e.wrap(client) for e in self.__endpoints})
