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
async def aioclient():
    c = binance.AIOClient()
    yield c
    await c.close()

@pytest.fixture(scope='module')
def client():
    c = binance.Client()
    yield c
    c.close()