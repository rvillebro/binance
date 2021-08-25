#!/usr/bin/env python3
from binance.utils import EnumStringMixin
from enum import Enum

class OrderType(EnumStringMixin, Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    STOP = 'STOP'
    STOP_MARKET = 'STOP_MARKET'
    TAKE_PROFIT = 'TAKE_PROFIT'
    TAKE_PROFIT_MARKET = 'TAKE_PROFIT_MARKET'
    TRAILING_STOP_MARKET = 'TRAILING_STOP_MARKET'


class OrderSide(EnumStringMixin, Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class PositionSide(EnumStringMixin, Enum):
    BOTH = 'BOTH'
    LONG = 'LONG'
    SHORT = 'SHORT'


class WorkingType(EnumStringMixin, Enum):
    MARK_PRICE = 'MARK_PRICE'
    CONTRACT_PRICE = 'CONTRACT_PRICE'


class TimeInForce(EnumStringMixin, Enum):
    GOOD_TILL_CANCEL = 'GTC'
    IMMEDIATE_OR_CANCEL = 'IOC'
    FILL_OR_KILL = 'FOK'
    GOOD_TILL_CROSSING = 'GTX'


class ResponseType(EnumStringMixin, Enum):
    ACK = 'ACK'
    RESULTS = 'RESULT'
