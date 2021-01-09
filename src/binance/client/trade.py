#!/usr/bin/env python3.8
import json

from binance import utils
from binance.enums import http, binance
from binance.order import Order

class Trade(object):
    """
    Class containing all trade related API entry points

    Args:
        client (binance.Client): client to use for API calls.
    """
    def __init__(self, client):
        self._client = client
    
    async def set_position_mode(self, dual_side_position, timestamp=None, receive_window=None):
        """
        Changes the user's position mode on every position: hedge mode or one-way mode (*TRADE*)

        https://binance-docs.github.io/apidocs/futures/en/#change-position-mode-trade

        Args:
            dual_side_position (str): True for hedge mode and False for one-way mode
            timestamp (int): timestamp
            receive_window (int): receive window
        """
        timestamp = timestamp if timestamp else utils.get_timestamp()

        params = utils.clean_params({
            'dualSidePosition': 'true' if dual_side_position else 'false',
            'timestamp': timestamp,
            'recvWindow': receive_window,
        })

        return await self._client._call(http.CallType.POST, '/fapi/v1/positionSide/dual', params=params, sign=True, use_api_key=True)

    async def get_position_mode(self, timestamp=None, receive_window=None):
        """
        Gets the user's position mode on every position: hedge mode or one-way mode (*USER_DATA*)

        https://binance-docs.github.io/apidocs/futures/en/#get-current-position-mode-user_data

        Args:
            timestamp (int): timestamp
            receive_window (int): receive window
        """
        timestamp = timestamp if timestamp else utils.get_timestamp()

        params = utils.clean_params({
            'timestamp': timestamp,
            'recvWindow': receive_window,
        })

        return await self._client._call(http.CallType.GET, '/fapi/v1/positionSide/dual', params=params, sign=True, use_api_key=True)
    
    async def new_order(self, order, timestamp=None, receive_window=None):
        """
        Send in a new order (*TRADE*).

        https://binance-docs.github.io/apidocs/futures/en/#new-order-trade

        Args:
            order (Order): a binance.order.Order object
            timestamp (int): timestamp
            receive_window (int): receive window
        """
        if not isinstance(order, Order):
            raise ValueError(f'order must be a binance.order.Order object')

        timestamp = timestamp if timestamp else utils.get_timestamp()

        params = order.params
        params['timestamp'] = timestamp
        params['recvWindow'] = receive_window
        params = utils.clean_params(params)
        print(params)

        return await self._client._call(http.CallType.POST, '/fapi/v1/order', params=params, sign=True, use_api_key=True)

    async def batch_order(self, orders, timestamp=None, receive_window=None):
        """
        Send in a batch of orders (*TRADE*).

        https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade

        Args:
            orders (Sequence[Order]): a list of binance.order.Order objects
        """
        if any([not isinstance(order, Order) for order in orders]):
            raise ValueError(f'orders must be a list of binance.order.Order objects')

        timestamp = timestamp if timestamp else utils.get_timestamp()

        params = utils.clean_params({
            'timestamp': timestamp,
            'recvWindow': receive_window,
        })
        params['batchOrders'] = list()
        for order in orders:
            order = utils.clean_params(order.params)
            params['batchOrders'].append(order)
        
        params['batchOrders'] = json.dumps(params['batchOrders'])
        print(params)

        #return await self._client._call(http.CallType.POST, '/fapi/v1/batchOrders', params=params, sign=True, use_api_key=True)
