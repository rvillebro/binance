"""
"""
from pydantic import BaseModel

class Stop(BaseModel):
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