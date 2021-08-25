#!/usr/vin/env python3.8
from binance.utils import EnumStringMixin
from enum import Enum

class Call(EnumStringMixin, Enum):
    GET = 'get'
    POST = 'post'

class ReturnCodes(EnumStringMixin, Enum):
    MALFORMEDREQUEST = "4xx"
    RATELIMIT = "429"
    IPBAN = "418"
    INTERNALERROR = "5xx"
    TIMEOUT = "503"  # might still be successful, it must be checked
