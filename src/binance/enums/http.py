#!/usr/vin/env python3.8
"""
HTTP enums
"""
from .base import StrEnum

class Method(StrEnum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class ReturnCodes(StrEnum):
    MALFORMEDREQUEST = "4xx"
    RATELIMIT = "429"
    IPBAN = "418"
    INTERNALERROR = "5xx"
    TIMEOUT = "503"  # might still be successful, it must be checked
