#!/usr/vin/env python3.8
"""
HTTP enums
"""
import requests
from .base import EnumString

class Method(EnumString):
    GET = 'GET'
    POST = 'POST'


class ReturnCodes(EnumString):
    MALFORMEDREQUEST = "4xx"
    RATELIMIT = "429"
    IPBAN = "418"
    INTERNALERROR = "5xx"
    TIMEOUT = "503"  # might still be successful, it must be checked
