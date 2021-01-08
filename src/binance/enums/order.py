#!/usr/bin/env python3.8
from enum import Enum

class OrderType(Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    STOP = 'STOP'
    STOP_MARKET = 'STOP_MARKET'
    TAKE_PROFIT = 'TAKE_PROFIT'
    TAKE_PROFIT_MARKET = 'TAKE_PROFIT_MARKET'
    TRAILING_STOP_MARKET = 'TRAILING_STOP_MARKET'

class OrderSide(Enum):
    BUY = 'BUY'
    SELL = 'SELL'

class PositionSide(Enum):
    BOTH = 'BOTH'
    LONG = 'LONG'
    SHORT = 'SHORT'

class TimeInForce(Enum):
    GOODTILLCANCEL = 'GTC'
    IMMEDIATEORCANCEL = 'IOC'
    FILLORKILL = 'FOK'
    GOODTILLCROSSING = 'GTX'

class ResponseType(Enum):
    ACK = 'ACK'
    RESULTS = 'RESULT'
