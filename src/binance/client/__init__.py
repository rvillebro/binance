#!/usr/bin/env python3.8
import os
import json
import hmac
import hashlib
import aiohttp
from types import SimpleNamespace

from binance.enums import http
from binance.constants import NETWORK
from .endpoints import market, trade

# load dot env environment variables (api key and secret)
from dotenv import load_dotenv
load_dotenv()

class Client(object):
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

        self.api_key = api_key
        self.api_secret = api_secret

        self.market = self.register_endpoints(market.endpoints)  # market API information
        self.trade = self.register_endpoints(trade.endpoints)  # trade API information

        self.session = aiohttp.ClientSession()

    def register_endpoints(self, endpoints):
        obj = SimpleNamespace()
        for endpoint in endpoints.list:
            setattr(obj, endpoint.func.__name__, endpoint.wrap(self))
        return obj

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def close(self) -> None:
        if self.session is not None:
            await self.session.close()
    
    async def _call(self, http_call: http.Call, route: str, /,
                    params=None, headers=None, api_key=False, sign=False):
        if api_key:
            headers = {} if headers is None else headers
            headers = self.__add_api_key_to_headers(headers)

        if sign:
            params['signature'] = self.__get_signature(params.urlencode())
        
        if http_call not in http.Call:
            raise ValueError(f'Call type unknown: {http_call}')
        
        call_function = getattr(self.session, http_call.value)
        if call_function:
            call = call_function(self._rest_base + route, params=params.urlencode(), headers=headers)

        async with call as response:
            status_code = response.status
            response_body = await response.text()
            if len(response_body) > 0:
                response_body = json.loads(response_body)

                return {
                    "status_code": status_code,
                    "response": response_body
                }
    
    def __add_api_key_to_headers(self, headers):
        headers.update({
            'X-MBX-APIKEY': self.api_key
        })

        return headers
    
    def __get_signature(self, params : str) -> str:
        signature = hmac.new(self.api_secret.encode(), params.encode(), hashlib.sha256).hexdigest()
        return signature
