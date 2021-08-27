#!/usr/bin/env python3
import pytest
import asyncio

import binance

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="module")
async def client():
    c = binance.Client()
    yield c
    await c.close()
