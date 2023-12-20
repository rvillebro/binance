"""
Asynchronous Binance API client
===============================
"""
import logging
from typing import TYPE_CHECKING

import aiohttp

from binance.client.base import BaseClient
from binance.enums import HTTPMethod

if TYPE_CHECKING:
    from binance.client.endpoints.base import APIParameters
    from binance.client.response import Response

log = logging.getLogger(__name__)


class AIOClient(BaseClient):
    """Asynchronous Binance client"""

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

    async def _call(
        self,
        http_method: HTTPMethod,
        route: str,
        /,
        params: "APIParameters" = None,
        headers: dict[str, str] = None,
        add_api_key: bool = False,
        add_signature: bool = False,
    ) -> "Response":
        if add_api_key is True:
            headers = self._add_api_key(headers)

        if add_signature is True:
            params = self._add_signature(params)

        log.debug("%s call at %s", self.api_url + route, http_method.value)
        response = await self.session.request(
            method=http_method.value, url=self.api_url + route, params=params.urlencode(), headers=headers
        )

        return await Response.from_aiohttp_response(response)
