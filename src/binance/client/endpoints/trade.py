"""
Trade endpoints
===============

https://binance-docs.github.io/apidocs/futures/en/#account-trades-endpoints
"""
from typing import Optional

import binance.utils as utils
from binance.order.base import Order

from .base import Endpoints, LinkEndpointsMixin


class Trade(LinkEndpointsMixin):
    endpoints = Endpoints()

    @endpoints.add('POST',
                   '/fapi/v1/positionSide/dual',
                   add_api_key=True,
                   add_signature=True)
    def set_position_mode(dualSidePosition,
                          timestamp: int = utils.get_timestamp,
                          recvWindow: Optional[int] = None):
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

    @endpoints.add('GET',
                   '/fapi/v1/positionSide/dual',
                   add_api_key=True,
                   add_signature=True)
    def get_position_mode(timestamp: int = utils.get_timestamp,
                          recvWindow: Optional[int] = None):
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
        pass

    @endpoints.add('POST',
                   '/fapi/v1/multiAssetsMargin',
                   add_api_key=True,
                   add_signature=True)
    def set_multiasset_mode(multiAssetsMargin,
                            timestamp: int = utils.get_timestamp,
                            recvWindow: int = None):
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
        pass

    @endpoints.add('GET', '/fapi/v1/multiAssetsMargin', add_api_key=True)
    def get_multiasset_mode(timestamp: int = utils.get_timestamp,
                            recvWindow: int = None):
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
        pass

    @endpoints.add('POST',
                   '/fapi/v1/order',
                   add_api_key=True,
                   add_signature=True)
    def new_order(order: Order,
                  timestamp: int = utils.get_timestamp,
                  recvWindow: int = None):
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
        pass

    def batch_order(orders: list[Order],
                    timestamp: int = utils.get_timestamp,
                    recvWindow: int = None):
        """
        Send in a batch of orders (*TRADE*).

        https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade

        Parameters
        ----------
        orders : list[binance.order.Order]
            list of binance.order.Order objects
        timestamp : int
            timestamp
        recvWindow : int
            receive window
        """
        pass
