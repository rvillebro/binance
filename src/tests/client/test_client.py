#!/usr/bin/env python3
import pytest

from binance import AIOClient


@pytest.mark.asyncio
async def test_client_initialization():
    c = AIOClient()
    await c.close()
