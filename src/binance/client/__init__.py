#!/usr/bin/env python3.8
import os
import json
import hmac
import hashlib
import aiohttp
import asyncio

from collections import OrderedDict

from binance.enums import http
from binance.constants import NETWORK

from .general import General
from .market import Market
from .trade import Trade

# load dot env environment variables (api key and secret)
from dotenv import load_dotenv
load_dotenv()

class Client(object):
    def __init__(self, api_key=os.environ.get('BINANCE_API_KEY'),
                 api_secret=os.environ.get('BINANCE_API_SECRET'),
                 mode=NETWORK.TEST, rest=None, websocket=None):
        if mode:
            self._rest_base = mode['REST']

        # overwrite base rest and websocket uri if defined
        if rest:
            self._rest_base = rest

        self.api_key = api_key
        self.api_secret = api_secret

        self.general = General(self)  # general API information
        self.market = Market(self)  # market API information
        self.trade = Trade(self)

        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def close(self) -> None:
        if self.session is not None:
            await self.session.close()
    
    async def _call(self, call_type: http.CallType, resource: str,
                    params=None, headers=None, use_api_key=False, sign=False):
        if use_api_key:
            headers = {} if headers is None else headers
            headers = self._add_api_key_to_headers(headers)

        if sign:
            params['signature'] = self._get_signature(params)
        
        if call_type not in http.CallType:
            raise ValueError(f'Call type unknown: {call_type}')
        
        call_function = getattr(self.session, call_type.function)
        if call_function:
            call = call_function(self._rest_base + resource, params = params, headers = headers)

        async with call as response:
            status_code = response.status
            response_body = await response.text()
            print(response.url)
            if len(response_body) > 0:
                response_body = json.loads(response_body)

                return {
                    "status_code": status_code,
                    "response": response_body
                }
    
    def _add_api_key_to_headers(self, headers):
        headers.update({
            'X-MBX-APIKEY': self.api_key
        })

        return headers
    
    def _get_signature(self, params : dict) -> str:
        params_string = ""

        if params:
            params_string = '&'.join([f"{key}={val}" for key, val in params.items()])

        signature = hmac.new(self.api_secret.encode(), params_string.encode(), hashlib.sha256).hexdigest()
        return signature
