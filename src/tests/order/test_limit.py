#!/usr/bin/env python3
import pytest

from binance.order.limit import Limit
from binance.enums import binance

def test_limit():
    """
    """
    o = Limit(symbol='BTCUSDT', side='BUY', quantity=1, price=1, timenInForce='GTC')
    print(o)