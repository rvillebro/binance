#!/usr/bin/env python3
import pytest

from binance import AIOClient, Client


def test_client_initialization():
    c = Client()
    c.close()


@pytest.mark.asyncio
async def test_aioclient_initialization():
    c = AIOClient()
    await c.close()
