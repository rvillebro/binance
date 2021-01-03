#!/usr/bin/env python3.8
import binance.client.utils as utils

from binance.enums import CallType

class General(object):
    def __init__(self, client):
        self._client = client

    async def ping(self):
        return await self._client._call(CallType.GET, '/fapi/v1/ping')
    
    async def server_time(self):
        return await self._client._call(CallType.GET, '/fapi/v1/time')
    
    async def exchange_info(self):
        return await self._client._call(CallType.GET, '/fapi/v1/exchangeInfo')
