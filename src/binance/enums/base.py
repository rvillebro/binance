#!/usr/bin/env python3
from enum import Enum

class EnumString(Enum):
    def __str__(self):
        return self.value
    
    @classmethod
    def _missing_(cls, value):
        value = value.upper()
        for member in cls:
            if member.value == value:
                return member
        return None