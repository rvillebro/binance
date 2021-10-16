#!/usr/bin/env python3
import json
import aiohttp

from binance.enums import http
from binance.client.base import BaseClient

class AIOClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.session = aiohttp.ClientSession()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def close(self) -> None:
        if self.session is not None:
            await self.session.close()
        
    async def _call(self, http_method: http.Method, route: str, /,
                    params=None, headers=None, add_api_key=False, add_signature=False):
        if add_api_key is True:
            if self._api_key is None:
                raise ValueError('Binance futures API key is missing!')
            headers = {} if headers is None else headers
            headers = self._add_api_key_to_headers(headers)

        if add_signature is True:
            if self._api_secret is None:
                raise ValueError('Binance futures API secret is missing!')
            params['signature'] = self._get_signature(params.urlencode())

        request = self.session.request(
            method=str(http_method),
            url=self._rest_base + route,
            params=params.urlencode(),
            headers=headers
        )

        async with request as response:
            status_code = response.status
            response_body = await response.text()
            if len(response_body) > 0:
                response_body = json.loads(response_body)

                return {
                    "status_code": status_code,
                    "response": response_body
                }
