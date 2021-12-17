"""
Binance ENUM definitions

https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info
"""
from .base import StrEnum

class SymbolType(StrEnum):
    FUTURE = 'FUTURE'


class ContractType(StrEnum):
    PERPETUAL = 'PERPETUAL'
    CURRENT_MONTH = 'CURRENT_MONTH'
    NEXT_MONTH = 'NEXT_MONTH'
    CURRENT_QUARTER = 'CURRENT_QUARTER'
    NEXT_QUARTER = 'NEXT_QUARTER'


class ContractStatus(StrEnum):
    PENDING_TRADING = 'PENDING_TRADING'
    TRADING = 'TRADING'
    PRE_DELIVERING = 'PRE_DELIVERING'
    DELIVERING = 'DELIVERING'
    DELIVERED = 'DELIVERED'
    PRE_SETTLE = 'PRE_SETTLE'
    SETTLING = 'SETTLING'
    CLOSE = 'CLOSE'


class OrderStatus(StrEnum):
    NEW = 'NEW'
    PARTIALLY_FILLED = 'PARTIALLY_FILLED'
    FILLED = 'FILLED'
    CANCELED = 'CANCELED'
    REJECTED = 'REJECTED'
    EXPIRED = 'EXPIRED'


class OrderType(StrEnum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    STOP = 'STOP'
    STOP_MARKET = 'STOP_MARKET'
    TAKE_PROFIT = 'TAKE_PROFIT'
    TAKE_PROFIT_MARKET = 'TAKE_PROFIT_MARKET'
    TRAILING_STOP_MARKET = 'TRAILING_STOP_MARKET'


class OrderSide(StrEnum):
    BUY = 'BUY'
    SELL = 'SELL'


class PositionSide(StrEnum):
    BOTH = 'BOTH'
    LONG = 'LONG'
    SHORT = 'SHORT'


class WorkingType(StrEnum):
    MARK_PRICE = 'MARK_PRICE'
    CONTRACT_PRICE = 'CONTRACT_PRICE'


class TimeInForce(StrEnum):
    GOOD_TILL_CANCEL = 'GTC'
    IMMEDIATE_OR_CANCEL = 'IOC'
    FILL_OR_KILL = 'FOK'
    GOOD_TILL_CROSSING = 'GTX'


class ResponseType(StrEnum):
    ACK = 'ACK'
    RESULTS = 'RESULT'


class KlineInterval(StrEnum):
    ONE_MINUTE = '1m'
    THREE_MINUTES = '3m'
    FIVE_MINUTES = '5m'
    FIFTEEN_MINUTES = '15m'
    THIRTY_MINUTES = '30m'
    ONE_HOURS = '1h'
    TWO_HOURS = '2h'
    FOUR_HOURS = '4h'
    SIX_HOURS = '6h'
    EIGHT_HOURS = '8h'
    TWELWE_HOURS = '12h'
    ONE_DAYS = '1d'
    THREE_DAYS = '3d'
    ONE_WEEK = '1w'
    ONE_MONTH = '1M'


class RateLimiter(StrEnum):
    REQUEST_WEIGHT = 'REQUEST_WEIGHT'
    ORDERS = 'ORDERS'


class RateLimitInterval(StrEnum):
    MINUTE = 'MINUTE'


class Period(StrEnum):
    FIVE_MINUTES = '5m'
    FIFTEEN_MINUTES = '15m'
    THIRTY_MINUTES = '30m'
    ONE_HOURS = '1h'
    TWO_HOURS = '2h'
    FOUR_HOURS = '4h'
    SIX_HOURS = '6h'
    EIGHT_HOURS = '8h'
    ONE_DAYS = '1d'
