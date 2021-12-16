from binance.order.base import Order
from typing import Optional
from binance import utils

class Trade:
    def set_position_mode(dualSidePosition, timestamp: int=utils.get_timestamp, recvWindow: Optional[int]=None):
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
    def get_position_mode(timestamp: int = ..., recvWindow: Optional[int] = ...):
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
    def set_multiasset_mode(multiAssetsMargin, timestamp: int = ..., recvWindow: int = ...):
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
    def get_multiasset_mode(timestamp: int = utils.timestamps, recvWindow: int = ...):
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
    def new_order(order: Order, timestamp: int = ..., recvWindow: int = ...):
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
    def batch_order(orders: list[Order], timestamp: int = ..., recvWindow: int = ...):
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
