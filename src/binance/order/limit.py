from typing import Optional, Literal
from pydantic import BaseModel

from binance.order.base import Order
from binance.enums import binance


class Limit(BaseModel, Order):
    """
    Initialize limit order object.

    Parameters
    ----------
    symbol : str
        symbol
    side : :class:`~binance.enum.binance.OrderSide`
        BUY or SELL
    positionSide : :class:`~binance.enum.binance.PositionSide`
        BOTH, LONG or SHORT. Default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
    timeInForce : :class:`~binance.enum.binance.TimeInForce`
        GTC (good till cancel), IOC (Immediate or Cancel), FOK (Fill or Kill) or GTX (Good Till Crossing, Post Only)
    quantity : float
        Cannot be sent with closePosition=true (Close-All)
    reduceOnly : str
        "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
    price : float
        Price 
    newClientOrderId : str
        A unique id among open binances. Automatically generated if not sent. Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
    reponseType :class:`~binance.enum.binance.ResponseType`
        "ACK" or "RESULT", default "ACK"
    """
    symbol : str
    side : binance.OrderSide
    quantity : float
    price : float
    timenInForce : binance.TimeInForce
    positionSide : Optional[binance.PositionSide] = None
    reduceOnly : Optional[str] = None
    clientOrderId : Optional[str] = None
    responseType : Optional[binance.ResponseType] = None
    type : Literal[binance.OrderType.LIMIT] = binance.OrderType.LIMIT

    class Config:
        use_enum_values = True