#!/usr/bin/env python3
from types import SimpleNamespace

NETWORK = SimpleNamespace(
    REAL = {
        'REST': 'https://fapi.binance.com',
        'WEBSOCKET': 'wss://fstream.binance.com',
    },
    TEST = {
        'REST': 'https://testnet.binancefuture.com',
        'WEBSOCKET': 'wss://stream.binancefuture.com',
    },
)