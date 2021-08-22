#!/usr/vin/env python3.8
from enum import Enum

class CallType(Enum):
    GET = 'get'
    POST = 'post'

class ReturnCodes(Enum):
    MALFORMEDREQUEST = "4xx"
    RATELIMIT = "429"
    IPBAN = "418"
    INTERNALERROR = "5xx"
    TIMEOUT = "503"  # might still be successful, it must be checked
