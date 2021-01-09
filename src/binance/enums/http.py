#!/usr/vin/env python3.8
from enum import Enum

class CallType(Enum):
    GET = 'get'
    POST = 'post'

    @property
    def function(self):
        return self.value
