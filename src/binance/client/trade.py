#!/usr/bin/env python3.8
<<<<<<< HEAD
import abc

from binance.client import utils
from binance.enums import http, order

class ORDER(abc.ABC):
    @property
    @abc.abstractmethod
    def params(self):
        raise NotImplementedError()

class LIMIT(ORDER):
    """
    Initializes limit order object.

    Args:
        symbol (str):
        side (enum): BUY or SELL
        position_side (enum): BOTH, LONG or SHORT. Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        time_in_force (enum): GTC (good till cancel), IOC (Immediate or Cancel), FOK (Fill or Kill) or GTX (Good Till Crossing, Post Only)
        quantity (float): Cannot be sent with closePosition=true (Close-All)
        reduce_only (str): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        price (float): 
        new_client_order_id (str): A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
        close_position (str): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        new_order_resp_type (enum): "ACK", "RESULT", default "ACK"
    """
    def __init__(
            self,
            symbol,
            side: order.OrderSide,
            position_side: order.PositionSide = None,
            time_in_force: order.TimeInForce = None,
            quantity: float = None,
            reduce_only: bool = None,
            price: float = None,
            new_client_order_id: str = None,
            close_position: bool = None,
            response_type: order.ResponseType = None,
        ):
        self.type = order.OrderType.LIMIT

        self.symbol = symbol
        self.side = side        
        self.position_side = position_side
        self.time_in_force = time_in_force
        self.quantity = quantity
        self.reduce_only = recude_only
        self.price = price
        self.close_position = close_position
        self.new_client_order_id = new_client_order_id
        self.new_order_resp_type = new_order_resp_type

class MARKET(ORDER):
    """
    Initializes market order object.

    Args:
        symbol (str):
        side (enum): BUY or SELL
        position_side (enum): BOTH, LONG or SHORT. Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        quantity (float): Cannot be sent with closePosition=true (Close-All)
        reduce_only (str): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        price (float): 
        new_client_order_id (str): A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
        close_position (str): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        new_order_resp_type (enum): "ACK", "RESULT", default "ACK"
    """
    def __init__(
            self,
            symbol,
            side: order.OrderSide,
            position_side: order.PositionSide = None,
            quantity: float = None,
            reduce_only: bool = None,
            price: float = None,
            new_client_order_id: str = None,
            close_position: bool = None,
            response_type: order.ResponseType = None,
        ):
        self.type = order.OrderType.MARKET

        self.symbol = symbol
        self.side = side        
        self.position_side = position_side
        self.quantity = quantity
        self.reduce_only = recude_only
        self.price = price
        self.close_position = close_position
        self.new_client_order_id = new_client_order_id
        self.new_order_resp_type = new_order_resp_type

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
