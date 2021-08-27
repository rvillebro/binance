#!/usr/bin/env python3
from enum import Enum

class EnumString(Enum):
    def __str__(self):
        return self.value