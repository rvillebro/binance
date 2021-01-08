#!/usr/bin/env python3.8
import binance.client.utils as utils

from binance.enums import CallType

class Trade(object):
    def __init__(self, client):
        self._client = client
    
    async def set_position_mode(self, dual_side_position, timestamp=None, receive_window=None):
            """
            Changes the user's position mode: hedge mode or one-way mode (*TRADE*)

            https://binance-docs.github.io/apidocs/futures/en/#change-position-mode-trade

            Args:
                dual_side_position (str): symbol to pull order book for.
                timestamp (int): timestamp
                receive_window (int): receive window
            """
            timestamp = timestamp if timestamp else utils.get_timestamp()

            params = utils.clean_params({
                'dualSidePosition': dual_side_position,
                'timestamp': timestamp,
                'recvWindow': receive_window,
            })

            return await self._client._call(CallType.POST, '/fapi/v1/positionSide/dual', params=params, sign=True, use_api_key=True)

    async def get_position_mode(self, timestamp=None, receive_window=None):
            """
            Gets the user's position mode: hedge mode or one-way mode (*USER_DATA*)

            https://binance-docs.github.io/apidocs/futures/en/#change-position-mode-trade

            Args:
                dual_side_position (str): symbol to pull order book for.
                timestamp (int): timestamp
                receive_window (int): receive window
            """
            timestamp = timestamp if timestamp else utils.get_timestamp()

            params = utils.clean_params({
                'timestamp': timestamp,
                'recvWindow': receive_window,
            })

            return await self._client._call(CallType.GET, '/fapi/v1/positionSide/dual', params=params, sign=True, use_api_key=True)
    
    async def get_position_information(self, symbol=None, timestamp=None, receive_window=None):
            timestamp = timestamp if timestamp else utils.get_timestamp()

            params = utils.clean_params({
                'symbol': symbol,
                'recvWindow': receive_window,
                'timestamp': timestamp,
            })

            return await self._client._call(CallType.GET, '/fapi/v1/positionRisk', params=params, sign=True, use_api_key=True)