"""
Trade
=====

https://binance-docs.github.io/apidocs/futures/en/#account-trades-endpoints
"""
from typing import Optional

import binance.client.endpoints.helpers as helpers
from binance.client.endpoints.base import Endpoints
from binance.client.response import Response
from binance.order.base import BatchOrder, OrderType

endpoints = Endpoints()


@endpoints.post("/fapi/v1/positionSide/dual", add_api_key=True, add_signature=True)
def set_position_mode(
    dualSidePosition, timestamp: int = helpers.get_timestamp, recvWindow: Optional[int] = None
) -> Response:
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


@endpoints.get("/fapi/v1/positionSide/dual", add_api_key=True, add_signature=True)
def get_position_mode(timestamp: int = helpers.get_timestamp, recvWindow: Optional[int] = None) -> Response:
    """
    Gets the user's position mode on every position: hedge mode or one-way mode (*USER_DATA*)

    https://binance-docs.github.io/apidocs/futures/en/#get-current-position-mode-user_data

    Parameters
    ----------
    timeStamp : int
        timestamp
    recvWindow : int
        receive window
    """


@endpoints.post("/fapi/v1/multiAssetsMargin", add_api_key=True, add_signature=True)
def set_multiasset_mode(multiAssetsMargin, timestamp: int = helpers.get_timestamp, recvWindow: int = None) -> Response:
    """
    Sets the user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol (*TRADE*)

    https://binance-docs.github.io/apidocs/futures/en/#change-multi-assets-mode-trade

    Parameters
    ----------
    multiAssetsMargin : bool
        "true" for Multi-Assets mode or "false" for Single-Assets mode
    timestamp : int
        timestamp
    recvWindow : int
        receive window
    """


@endpoints.get("/fapi/v1/multiAssetsMargin", add_api_key=True)
def get_multiasset_mode(timestamp: int = helpers.get_timestamp, recvWindow: int = None) -> Response:
    """
    Gets the user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol (*USER DATA*)

    https://binance-docs.github.io/apidocs/futures/en/#get-current-multi-assets-mode-user_data

    Parameters
    ----------
    timestamp : int
        timestamp
    recvWindow : int
        receive window
    """


@endpoints.post("/fapi/v1/order", add_api_key=True, add_signature=True)
def new_order(order: OrderType, timestamp: int = helpers.get_timestamp, recvWindow: int = None) -> Response:
    """
    Send in a new order (*TRADE*).

    https://binance-docs.github.io/apidocs/futures/en/#new-order-trade

    Parameters
    ----------
    order : :class:`~binance.order.Order`
        An :class:`~binance.order.Order` object
    timestamp : int
        timestamp
    recvWindow : int
        receive window
    """


@endpoints.post("/fapi/v1/batchOrders", add_api_key=True, add_signature=True)
def batch_order(orders: BatchOrder, timestamp: int = helpers.get_timestamp, recvWindow: int = None) -> Response:
    """
    Send in a batch of orders (*TRADE*).

    https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade

    Parameters
    ----------
    orders: :class:`binance.order.BatchOrder`
        Batch order to send
    timestamp: int
        timestamp
    recvWindow: int
        receive window
    """


if __name__ == "__main__":
    import doctest

    from binance.client import Client

    doctest.testmod(globs=dict(client=Client()), optionflags=doctest.ELLIPSIS)
