#!/usr/bin/env python3
import pytest

from binance import Client


@pytest.mark.asyncio
async def test_client_initialization():
    c = Client()
    await c.close()
