"""
"""
from pydantic import BaseModel


class Market(BaseModel):
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
