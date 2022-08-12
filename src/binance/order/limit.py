from typing import TYPE_CHECKING, Optional, Literal, overload
from pydantic import ValidationError, constr, validator

from binance.order.base import Order
from binance.enums import binance

if TYPE_CHECKING:
    from binance.client import Client, AIOClient


class Limit(Order):
    """
    Initialize limit order object.

    Parameters
    ----------
    symbol: str
        symbol
    side: :class:`~binance.enum.binance.OrderSide`
        BUY or SELL
    positionSide: :class:`~binance.enum.binance.PositionSide`
        BOTH, LONG or SHORT.
        Default BOTH for One-way Mode; LONG or SHORT for Hedge Mode.
        It must be sent in Hedge Mode.
    timeInForce: :class:`~binance.enum.binance.TimeInForce`
        GTC (good till cancel), IOC (Immediate or Cancel), FOK (Fill or Kill) or GTX (Good Till Crossing, Post Only)
    quantity: float, optional
        Cannot be sent with closePosition=true (Close-All)
    reduceOnly: str, optional
        "true" or "false".
        Default "false".
        Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
    price: float, optional
        Price 
    newClientOrderId: str, optional
        A unique id among open binances.
        Automatically generated if not sent.
        Can only be string following the rule: ^[a-zA-Z0-9-_]{1,36}$
    reponseType: :class:`~binance.enum.binance.ResponseType`, optional
        "ACK" or "RESULT", default "ACK"
    """
    symbol: str
    side: binance.OrderSide
    quantity: float
    price: float
    timeInForce: binance.TimeInForce
    positionSide: Optional[binance.PositionSide] = None
    reduceOnly: Optional[bool] = None
    clientOrderId: Optional[constr(regex=r'^[\.A-Z\:/a-z0-9_-]{1,36}$')] = None
    responseType: Optional[binance.ResponseType] = None
    type: Literal[binance.OrderType.LIMIT] = binance.OrderType.LIMIT

'''
    @validator('positionSide', always=True)
    def hedgemode_mandatory(cls, v):
        if 'in_hedgemode' and v is None:
            raise ValidationError('positionSide must be set in hedgemode', cls)
        return v

    @validator('reduceOnly')
    def oneway_only(cls, v):
        if 'in_hedgemode':
            raise ValidationError('reduceOnly cannot be set in hedgemode')
        return v

    @overload
    async def validate(self, client: 'AIOClient'):
        """
        Validates order against client

        Parameters
        ----------
        client : binance.client.AIOClient
            Binance client
        """
        client.trade.get_position_mode()

        if self.positionSide:
            pass

        return True

    def validate(self, client: 'Client'):
        """
        Validates order against client

        Parameters
        ----------
        client : binance.client.AIOClient
            Binance client
        """
        dual_pos = client.trade.get_position_mode().data["dualSidePosition"]

        if dual_pos:
            if self.positionSide is None:
                raise ValidationError('positionSide must be set in hedgemode')

            if self.reduceOnly:
                raise ValidationError('reduceOnly cannot be set in hedgemode')

        return True
'''