import os
import re
import abc
import hmac
import hashlib

from dotenv import load_dotenv
from typing import TYPE_CHECKING

from binance.enums import http, binance
from binance.constants import NETWORK
from binance.client import endpoints

if TYPE_CHECKING:
    from aiohttp import ClientResponse as AIOHTTPResponse
    from requests import Response as RequestsResponse

load_dotenv()


class BaseClient(abc.ABC):
    #: indicates whether endpoints should be asynchronous
    ASYNCHRONOUS: bool

    def __init__(self,
                 api_key: str = os.environ.get('BINANCE_API_KEY'),
                 api_secret: str = os.environ.get('BINANCE_API_SECRET'),
                 mode=NETWORK.TEST,
                 rest=None,
                 websocket=None):
        if mode:
            self._rest_base = mode['REST']
            self._websocket_base = mode['WEBSOCKET']

        # overwrite base rest and websocket uri if defined
        if rest:
            self._rest_base = rest
        if websocket:
            self._websocket_base = websocket

        self._api_key = api_key
        self._api_secret = api_secret

        self.market = endpoints.Market.link(self)
        self.trade = endpoints.Trade.link(self)
        self.user_data = endpoints.UserData.link(self)

    def _add_api_key(self, headers: dict) -> dict:
        """Adds API key to headers"""
        if self._api_key is None:
            raise ValueError('Binance futures API key is missing!')
        headers = dict() if headers is None else headers
        headers.update({'X-MBX-APIKEY': self._api_key})
        return headers

    def _add_signature(self, params: '_Parameters') -> str:
        """Adds signature to params"""
        if self._api_secret is None:
            raise ValueError('Binance futures API secret is missing!')
        url_encoded_params = params.urlencode()
        signature = hmac.new(self._api_secret.encode(),
                             url_encoded_params.encode(),
                             hashlib.sha256).hexdigest()
        params['signature'] = signature
        return params

    @abc.abstractmethod
    def _call(self,
              http_method: http.Method,
              route: str,
              /,
              params=None,
              headers=None,
              add_api_key=False,
              add_signature=False) -> None:
        """HTTP request."""


class ResponseException(Exception):

    def __init__(self, status: int, reason: str, data: dict, raw: object):
        self.status = status
        self.reason = reason
        self.data = data
        self.raw = raw

    def __str__(self):
        return f"HTTP status code '{self.status}': {self.reason} ({self.data})"


class Response:
    REQUEST_WEIGHT = re.compile(r'X-MBX-USED-WEIGHT-.*')
    ORDERS = re.compile(r'X-MBX-ORDER-COUNT-.*')

    def __init__(self, data: dict, status: int, limits: dict,
                 raw: object) -> object:
        self.data = data
        self.status = status
        self.limits = limits
        self.raw = raw

    @staticmethod
    def get_limits(headers):
        limits = dict()
        for key, val in headers.items():
            if key.startswith('X-MBX-USED-WEIGHT-') or key.startswith(
                    'X-MBX-ORDER-COUNT-'):
                limits[key] = val
        return limits

    @classmethod
    async def from_aiohttp_response(cls, response: 'AIOHTTPResponse'):
        if not response.ok:
            raise ResponseException(status=response.status,
                                    reason=response.reason,
                                    dict=await response.json(),
                                    raw=response)

        data = await response.json()
        limits = cls.get_limits(response.headers)
        return cls(data=data,
                   status=response.status,
                   limits=limits,
                   raw=response)

    @classmethod
    def from_requests_response(cls, response: 'RequestsResponse'):
        if not response.ok:
            raise ResponseException(status=response.status_code,
                                    reason=response.reason,
                                    data=response.json(),
                                    raw=response)

        data = response.json()
        limits = cls.get_limits(response.headers)
        limits = cls.get_limits(response.headers)
        return cls(data=data,
                   status=response.status_code,
                   limits=limits,
                   raw=response)

    def __repr__(self):
        return f"Response(status={self.status}, data={self.data})"
