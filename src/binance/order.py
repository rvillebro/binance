#!/usr/bin/env python3
from binance.enums import binance

class Order(object):
    PARAM_NAMES = {
        'position_side': 'positionSide',
        'time_in_force': 'timeInForce',
        'reduce_only': 'reduce_only',
        'client_order_id': 'newClientOrderId',
        'stop_price': 'stopPrice',
        'close_position': 'closePosition',
        'activation_price': 'activationPrice',
        'callback_rate': 'callbackRate',
        'working_type': 'workingType',
        'price_protect': 'priceProtect',
        'response_type': 'newOrderRespType',
    }

    @property
    def params(self):
        params = dict()
        for param in self.__slots__:
            name = self.PARAM_NAMES.get(param, param)
            params[name] = getattr(self, param)
        return params

class Limit(Order):
    """
    Initializes limit binance object.

    Args:
        symbol (str):
        side (enum): BUY or SELL
        position_side (enum): BOTH, LONG or SHORT. Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        time_in_force (enum): GTC (good till cancel), IOC (Immediate or Cancel), FOK (Fill or Kill) or GTX (Good Till Crossing, Post Only)
        quantity (float): Cannot be sent with closePosition=true (Close-All)
        reduce_only (str): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        price (float): 
        client_order_id (str): A unique id among open binances. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
        close_position (str): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        reponse_type (enum): "ACK", "RESULT", default "ACK"
    """
    __slots__ = (
        'type',
        'symbol',
        'side',
        'quantity',
        'price',
        'time_in_force',
        'position_side',
        'reduce_only',
        'client_order_id',
        'close_position',
        'response_type',
    )

    def __init__(
            self,
            symbol,
            side: binance.OrderSide,
            quantity: float,
            price: float,
            time_in_force: binance.TimeInForce,
            position_side: binance.PositionSide = None,
            reduce_only: bool = None,
            client_order_id: str = None,
            close_position: bool = None,
            response_type: binance.ResponseType = None,
        ):
        self.type = binance.OrderType.LIMIT

        self.symbol = symbol
        self.side = side
        self.position_side = position_side
        self.time_in_force = time_in_force
        self.quantity = quantity
        self.reduce_only = reduce_only
        self.price = price
        self.close_position = close_position
        self.client_order_id = client_order_id
        self.response_type = response_type


class Market(Order):
    """
    Initializes market binance object.

    Args:
        symbol (str):
        side (enum): BUY or SELL
        position_side (enum): BOTH, LONG or SHORT. Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        quantity (float): Cannot be sent with closePosition=true (Close-All)
        reduce_only (str): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        close_position (str): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        client_order_id (str): A unique id among open binances. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
        response_type (enum): "ACK", "RESULT", default "ACK"
    """
    __slots__ = ['type', 'symbol', 'side', 'position_side', 'quantity', 'reduce_only', 'close_position', 'client_order_id', 'response_type']

    def __init__(
            self,
            symbol,
            side: binance.OrderSide,
            quantity: float,
            position_side: binance.PositionSide = None,
            reduce_only: bool = None,
            close_position: bool = None,
            client_order_id: str = None,
            response_type: binance.ResponseType = None,
        ):
        self.type = binance.OrderType.MARKET

        # check enums
        if isinstance(side, binance.OrderSide):
            self.side = side
        else:
            raise ValueError(f'{side} is not a valid binance OrderSide.')
        if isinstance(position_side, binance.PositionSide) or position_side is None:
            self.position_side = position_side
        else:
            raise ValueError(f'{position_side} is not a valid binance PositionSide.')
        if isinstance(response_type, binance.ResponseType) or response_type is None:
            self.response_type = response_type
        else:
            raise ValueError(f'{response_type} is not a valid binance ResponseType.')

        self.symbol = symbol
        self.quantity = quantity
        self.reduce_only = reduce_only
        self.close_position = close_position
        self.client_order_id = client_order_id


class Stop(Order):
    """
    Initializes stop binance object.

    Args:
        symbol (str):
        side (enum): BUY or SELL
        quantity (float): Cannot be sent with closePosition=true (Close-All)
        price (float): price
        stop_price (float): Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET binances.
        position_side (enum): BOTH, LONG or SHORT. Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        price_protect (bool): "TRUE" or "FALSE", default "FALSE". Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET binances.
        working_type (enum): stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"
        time_in_force (enum): GTC (good till cancel), IOC (Immediate or Cancel), FOK (Fill or Kill) or GTX (Good Till Crossing, Post Only)
        reduce_only (str): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        close_position (str): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        client_order_id (str): A unique id among open binances. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
        response_type (enum): "ACK", "RESULT", default "ACK"
    """
    def __init__(
            self,
            symbol,
            side: binance.OrderSide,
            quantity: float,
            price: float,
            stop_price: float,
            position_side: binance.PositionSide = None,
            price_protect: bool = None,
            working_type: binance.WorkingType = None,
            time_in_force: binance.TimeInForce = None,
            reduce_only: bool = None,
            close_position: bool = None,
            client_order_id: str = None,
            response_type: binance.ResponseType = None,
        ):
        self.type = binance.OrderType.STOP

        self.symbol = symbol
        self.side = side
        self.quantity = quantity
        self.price = price
        self.stop_price = stop_price
        self.position_side = position_side
        self.price_protect = price_protect
        self.working_type = working_type
        self.time_in_force = time_in_force
        self.reduce_only = reduce_only
        self.close_position = close_position
        self.client_order_id = client_order_id
        self.response_type = response_type


class StopMarket(Order):
    """
    Initializes stop market binance object.

    Args:
        symbol (str):
        side (enum): BUY or SELL
        stop_price (float): Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET binances.
        quantity (float): Cannot be sent with closePosition=true (Close-All)
        position_side (enum): BOTH, LONG or SHORT. Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        price_protect (bool): "TRUE" or "FALSE", default "FALSE". Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET binances.
        working_type (enum): stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"
        time_in_force (enum): GTC (good till cancel), IOC (Immediate or Cancel), FOK (Fill or Kill) or GTX (Good Till Crossing, Post Only)
        reduce_only (str): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        close_position (str): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        client_order_id (str): A unique id among open binances. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
        response_type (enum): "ACK", "RESULT", default "ACK"
    """
    def __init__(
            self,
            symbol,
            side: binance.OrderSide,
            stop_price: float,
            quantity: float = None,
            position_side: binance.PositionSide = None,
            price_protect: bool = None,
            working_type: binance.WorkingType = None,
            time_in_force: binance.TimeInForce = None,
            reduce_only: bool = None,
            close_position: bool = None,
            client_order_id: str = None,
            response_type: binance.ResponseType = None,
        ):
        self.type = binance.OrderType.STOP_MARKET

        self.symbol = symbol
        self.side = side
        self.stop_price = stop_price
        self.position_side = position_side
        self.price_protect = price_protect
        self.working_type = working_type
        self.time_in_force = time_in_force
        self.reduce_only = reduce_only
        self.close_position = close_position
        self.client_order_id = client_order_id
        self.response_type = response_type


class TakeProfit(Order):
    """
    Initializes take profit binance object.

    Args:
        symbol (str):
        side (enum): BUY or SELL
        quantity (float): Cannot be sent with closePosition=true (Close-All)
        price (float): price
        stop_price (float): Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET binances.
        position_side (enum): BOTH, LONG or SHORT. Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        price_protect (bool): "TRUE" or "FALSE", default "FALSE". Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET binances.
        working_type (enum): stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"
        time_in_force (enum): GTC (good till cancel), IOC (Immediate or Cancel), FOK (Fill or Kill) or GTX (Good Till Crossing, Post Only)
        reduce_only (str): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        close_position (str): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        client_order_id (str): A unique id among open binances. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
        response_type (enum): "ACK", "RESULT", default "ACK"
    """
    def __init__(
            self,
            symbol,
            side: binance.OrderSide,
            quantity: float,
            price: float,
            stop_price: float,
            position_side: binance.PositionSide = None,
            price_protect: bool = None,
            working_type: binance.WorkingType = None,
            time_in_force: binance.TimeInForce = None,
            reduce_only: bool = None,
            close_position: bool = None,
            client_order_id: str = None,
            response_type: binance.ResponseType = None,
        ):
        self.type = binance.OrderType.TAKE_PROFIT

        self.symbol = symbol
        self.side = side
        self.quantity = quantity
        self.price = price
        self.stop_price = stop_price
        self.position_side = position_side
        self.price_protect = price_protect
        self.working_type = working_type
        self.time_in_force = time_in_force
        self.reduce_only = reduce_only
        self.close_position = close_position
        self.client_order_id = client_order_id
        self.response_type = response_type


class TakeProfitMarket(Order):
    """
    Initializes take profit market binance object.

    Args:
        symbol (str):
        side (enum): BUY or SELL
        stop_price (float): Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET binances.
        quantity (float): Cannot be sent with closePosition=true (Close-All)
        position_side (enum): BOTH, LONG or SHORT. Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        price_protect (bool): "TRUE" or "FALSE", default "FALSE". Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET binances.
        working_type (enum): stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"
        time_in_force (enum): GTC (good till cancel), IOC (Immediate or Cancel), FOK (Fill or Kill) or GTX (Good Till Crossing, Post Only)
        reduce_only (str): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        close_position (str): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        client_order_id (str): A unique id among open binances. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
        response_type (enum): "ACK", "RESULT", default "ACK"
    """
    def __init__(
            self,
            symbol,
            side: binance.OrderSide,
            stop_price: float,
            quantity: float = None,
            position_side: binance.PositionSide = None,
            price_protect: bool = None,
            working_type: binance.WorkingType = None,
            time_in_force: binance.TimeInForce = None,
            reduce_only: bool = None,
            close_position: bool = None,
            client_order_id: str = None,
            response_type: binance.ResponseType = None,
        ):
        self.type = binance.OrderType.TAKE_PROFIT_MARKET

        self.symbol = symbol
        self.side = side
        self.stop_price = stop_price
        self.position_side = position_side
        self.price_protect = price_protect
        self.working_type = working_type
        self.time_in_force = time_in_force
        self.reduce_only = reduce_only
        self.close_position = close_position
        self.client_order_id = client_order_id
        self.response_type = response_type
