#!/usr/bin/env python3.8
from enum import Enum

class ReturnCodes(Enum):
    MALFORMEDREQUEST = "4xx"
    RATELIMIT = "429"
    IPBAN = "418"
    INTERNALERROR = "5xx"
    TIMEOUT = "503"  # might still be successful, it must be checked

class OrderType(Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    STOP = 'STOP'
    STOP_MARKET = 'STOP_MARKET'
    TAKE_PROFIT = 'TAKE_PROFIT'
    TAKE_PROFIT_MARKET = 'TAKE_PROFIT_MARKET'
    TRAILING_STOP_MARKET = 'TRAILING_STOP_MARKET'

    def __str__(self):
        return self.value

class OrderSide(Enum):
    BUY = 'BUY'
    SELL = 'SELL'

    def __str__(self):
        return self.value

class PositionSide(Enum):
    BOTH = 'BOTH'
    LONG = 'LONG'
    SHORT = 'SHORT'

    def __str__(self):
        return self.value

class WorkingType(Enum):
    MARK_PRICE = 'MARK_PRICE'
    CONTRACT_PRICE = 'CONTRACT_PRICE'

class TimeInForce(Enum):
    GOOD_TILL_CANCEL = 'GTC'
    IMMEDIATE_OR_CANCEL = 'IOC'
    FILL_OR_KILL = 'FOK'
    GOOD_TILL_CROSSING = 'GTX'

class ResponseType(Enum):
    ACK = 'ACK'
    RESULTS = 'RESULT'

    def __str__(self):
        return self.value
