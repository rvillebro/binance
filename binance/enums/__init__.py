import sys
from enum import auto

from binance.enums import binance

if sys.version_info < (3, 11):
    from strenum import StrEnum
else:
    from enum import StrEnum


__all__ = ["HTTPMethod", "binance"]


class HTTPMethod(StrEnum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
