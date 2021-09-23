#!/usr/bin/env python3
import os
import abc
import json
import hmac
import hashlib

from types import SimpleNamespace

from binance.enums import http
from binance.constants import NETWORK
from .endpoints import market, trade

# load dot env environment variables (api key and secret)
from dotenv import load_dotenv
load_dotenv()

class BaseClient(abc.ABC):
    def __init__(self, api_key=os.environ.get('BINANCE_API_KEY'),
                 api_secret=os.environ.get('BINANCE_API_SECRET'),
                 mode=NETWORK.TEST, rest=None, websocket=None):
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

        self.market = self.register_endpoints(market.endpoints)  # market API information
        self.trade = self.register_endpoints(trade.endpoints)  # trade API information

    def register_endpoints(self, endpoints):
        obj = SimpleNamespace()
        for endpoint in endpoints.to_list():
            setattr(obj, endpoint.func.__name__, endpoint.wrap(self))
        return obj
    
    def _add_api_key_to_headers(self, headers):
        headers.update({
            'X-MBX-APIKEY': self._api_key
        })

        return headers
    
    def _get_signature(self, params : str) -> str:
        signature = hmac.new(self._api_secret.encode(), params.encode(), hashlib.sha256).hexdigest()
        return signature

    @abc.abstractmethod
    def _call(self, http_method: http.Method, route: str, /,
              params=None, headers=None, add_api_key=False,
              add_signature=False) -> None:
        """HTTP request."""