#!/usr/bin/env python3
import pytest

import binance.client
from binance.order.limit import Limit
from binance.enums import binance


def test_limit(client):
    """
    """
    pytest.skip()
    o = Limit(symbol='BTCUSDT',
              side='BUY',
              quantity=0.1,
              price=36000,
              timeInForce='GTC')

    client.trade.new_order(order=o)
    print(o.dict(exclude_none=True))
