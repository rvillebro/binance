#!/usr/bin/env python3
"""
Trade data endpoints

https://binance-docs.github.io/apidocs/futures/en/#account-trades-endpoints
"""
import binance.utils as utils
from binance.order import Order

from . import Endpoints

endpoints = Endpoints('trade')

@endpoints.add('post', '/fapi/v1/positionSide/dual', add_api_key=True, add_signature=True)
def set_position_mode(dualSidePosition, timestamp=utils.get_timestamp(), receiveWindow=None):
    """
    Sets the user's position mode on every position: hedge mode or one-way mode (*TRADE*)

    https://binance-docs.github.io/apidocs/futures/en/#change-position-mode-trade

    Parameters
    ----------
    dualSidePosition : str
        "true" for hedge mode and "false" for one-way mode
    timeStamp : int
        timestamp
    receiveWindow : int
        receive window
    """
    pass


@endpoints.add('get', '/fapi/v1/positionSide/dual', add_api_key=True, add_signature=True)
def get_position_mode(timestamp=utils.get_timestamp(), receiveWindow=None):
    """
    Gets the user's position mode on every position: hedge mode or one-way mode (*USER_DATA*)

    https://binance-docs.github.io/apidocs/futures/en/#get-current-position-mode-user_data

    Parameters
    ----------
    timeStamp : int
        timestamp
    receiveWindow : int
        receive window
    """
    pass

    
def new_order(order: Order, timestamp=utils.get_timestamp(), receive_window=None):
    """
    Send in a new order (*TRADE*).

    https://binance-docs.github.io/apidocs/futures/en/#new-order-trade

    Parameters
    ----------
    order : binance.order.Order
        a binance.order.Order object
    timestamp : int
        timestamp
    receive_window : int
        receive window
    """
    pass

def batch_order(orders: list[Order], timestamp=utils.get_timestamp(), receive_window=None):
    """
    Send in a batch of orders (*TRADE*).

    https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade

    Parameters
    ----------
    orders : list[binance.order.Order]
        list of binance.order.Order objects
    timestamp : int
        timestamp
    receive_window : int
        receive window
    """
    pass
