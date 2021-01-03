#!/usr/bin/env python3.8
from enum import Enum

class CallType(Enum):
    GET = 'get'
    POST = 'post'

    @property
    def function(self):
        return self.value

class ReturnCodes(Enum):
    MALFORMEDREQUEST = "4xx"
    RATELIMIT = "429"
    IPBAN = "418"
    INTERNALERROR = "5xx"
    TIMEOUT = "503"  # might still be successful, it must be checked