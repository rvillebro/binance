#!/usr/bin/env python3
from typing import TYPE_CHECKING

import pytest

from binance.order.limit import Limit

if TYPE_CHECKING:
    from binance.client import Client


def test_limit(client: "Client"):
    """ """
    pytest.skip()
    o = Limit(symbol="BTCUSDT", side="BUY", quantity=0.1, price=1, timeInForce="GTC")

    client.trade.new_order(order=o)
    print(o.dict(exclude_none=True))
