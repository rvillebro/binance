#!/usr/bin/env python3.8
import json
import aiohttp
import asyncio

from binance import enums
from binance.constants import REST_API_URL

from .general import General
from .market import Market

class Client(object):
    def __init__(self, api_key, api_secret, base_url = REST_API_URL.FUTURES_TEST):
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.general = General(self)  # general API information
        self.market = Market(self)

        self.session = aiohttp.ClientSession()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def close(self) -> None:
        if self.session is not None:
            await self.session.close()
    
    async def _call(self, call_type: enums.CallType, resource: str, data=None, params=None, headers=None, use_api_key=False, sign=False):
        if use_api_key:
            headers = self._add_api_key_to_headers(headers)

        if sign:
            data = {} if data is None else data
            params = {} if params is None else params
            params['signature'] = self._get_signature(params, data)
        
        if call_type not in enums.CallType:
            raise ValueError(f'Call type unknown: {call_type}')

        call_function = getattr(self.session, call_type.function)
        if call_function:
            call = call_function(self.base_url + resource, json = data, params = params, headers = headers)
        
        async with call as response:
            status_code = response.status
            response_body = await response.text()

            if len(response_body) > 0:
                response_body = json.loads(response_body)

                return {
                    "status_code": status_code,
                    "response": response_body
                }
    
    def _add_api_key_to_headers(self, headers):
        headers.update({
            'Accept': 'application/json',
            'X-MBX-APIKEY': self.api_key
        })

        return headers
    
    def _get_signature(self, params : dict, data : dict) -> str:
        params_string = ""
        data_string = ""

        if params:
            params_string = '&'.join([f"{key}={val}" for key, val in params.items()])

        if data:
            data_string = '&'.join(["{}={}".format(param[0], param[1]) for param in data])

        m = hmac.new(self.api_secret.encode('utf-8'), (params_string+data_string).encode('utf-8'), hashlib.sha256)
        return m.hexdigest()
