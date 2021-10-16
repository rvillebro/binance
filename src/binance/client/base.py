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
        for e in endpoints:
            setattr(obj, e.func.__name__, e.wrap(self))
        return obj
    
    def _add_api_key(self, headers):
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
        signature = hmac.new(self._api_secret.encode(), url_encoded_params.encode(), hashlib.sha256).hexdigest()
        params['signature'] = signature
        return params

    @abc.abstractmethod
    def _call(self, http_method: http.Method, route: str, /,
              params=None, headers=None, add_api_key=False,
              add_signature=False) -> None:
        """HTTP request."""