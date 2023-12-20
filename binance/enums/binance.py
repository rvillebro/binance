"""
Binance ENUM definitions

https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info
"""
import sys
from enum import auto

if sys.version_info < (3, 11):
    from strenum import StrEnum
else:
    from enum import StrEnum


class SymbolType(StrEnum):
    FUTURE = "FUTURE"


class ContractType(StrEnum):
    PERPETUAL = auto()
    CURRENT_MONTH = auto()
    NEXT_MONTH = auto()
    CURRENT_QUARTER = auto()
    NEXT_QUARTER = auto()
    PERPETUAL_DELIVERING = auto()


class ContractStatus(StrEnum):
    PENDING_TRADING = auto()
    TRADING = auto()
    PRE_DELIVERING = auto()
    DELIVERING = auto()
    DELIVERED = auto()
    PRE_SETTLE = auto()
    SETTLING = auto()
    CLOSE = auto()


class OrderStatus(StrEnum):
    NEW = auto()
    PARTIALLY_FILLED = auto()
    FILLED = auto()
    CANCELED = auto()
    REJECTED = auto()
    EXPIRED = auto()
    EXPIRED_IN_MATCH = auto()


class OrderType(StrEnum):
    LIMIT = auto()
    MARKET = auto()
    STOP = auto()
    STOP_MARKET = auto()
    TAKE_PROFIT = auto()
    TAKE_PROFIT_MARKET = auto()
    TRAILING_STOP_MARKET = auto()


class OrderSide(StrEnum):
    BUY = auto()
    SELL = auto()


class PositionSide(StrEnum):
    BOTH = auto()
    LONG = auto()
    SHORT = auto()


class WorkingType(StrEnum):
    MARK_PRICE = auto()
    CONTRACT_PRICE = auto()


class TimeInForce(StrEnum):
    GOOD_TILL_CANCEL = "GTC"
    IMMEDIATE_OR_CANCEL = "IOC"
    FILL_OR_KILL = "FOK"
    GOOD_TILL_CROSSING = "GTX"
    GOOD_TILL_DATA = "GTD"


class WorkingType(StrEnum):
    MARK_PRICE = auto()
    CONTRACT_PRICE = auto()


class ResponseType(StrEnum):
    ACK = auto()
    RESULT = auto()


class KlineInterval(StrEnum):
    ONE_MINUTE = "1m"
    THREE_MINUTES = "3m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    SIX_HOURS = "6h"
    EIGHT_HOURS = "8h"
    TWELWE_HOURS = "12h"
    ONE_DAY = "1d"
    THREE_DAYS = "3d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1M"


class STPMode(StrEnum):
    NONE = auto()
    EXPIRE_TAKER = auto()
    EXPIRE_BOTH = auto()
    EXPIRE_MAKER = auto()


class PriceMatch(StrEnum):
    NONE = auto()
    OPPONENT = auto()
    OPPONENT_5 = auto()
    OPPONENT_10 = auto()
    OPPONENT_20 = auto()
    QUEUE = auto()
    QUEUE_5 = auto()
    QUEUE_10 = auto()
    QUEUE_20 = auto()


class RateLimiter(StrEnum):
    REQUEST_WEIGHT = "X-MBX-USED-WEIGHT-"
    ORDERS = "X-MBX-ORDER-COUNT-"


class RateLimitInterval(StrEnum):
    MINUTE = auto()


class Period(StrEnum):
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    SIX_HOURS = "6h"
    EIGHT_HOURS = "8h"
    ONE_DAY = "1d"
