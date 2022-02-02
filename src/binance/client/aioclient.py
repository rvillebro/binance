"""
Asynchronous Binance API client
===============================
"""
import json
import aiohttp

from binance.enums import http
from binance.client.base import BaseClient, Response


class AIOClient(BaseClient):
    ASYNCHRONOUS = True

    def __init__(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()
        super().__init__(*args, *kwargs)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def close(self) -> None:
        if self.session is not None:
            await self.session.close()

    async def _call(self,
                    http_method: http.Method,
                    route: str,
                    /,
                    params=None,
                    headers=None,
                    add_api_key=False,
                    add_signature=False):
        """
        Returns
        -------
        https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientResponse
        """
        if add_api_key is True:
            headers = self._add_api_key(headers)

        if add_signature is True:
            params = self._add_signature(params)

        response = await self.session.request(method=http_method.value,
                                              url=self._rest_base + route,
                                              params=params.urlencode(),
                                              headers=headers)

        return await Response.from_aiohttp_response(response)
