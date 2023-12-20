"""
"""
from types import SimpleNamespace

NETWORK = SimpleNamespace(
    REAL={
        "API": "https://fapi.binance.com",
        "WEBSOCKET": "wss://fstream.binance.com",
    },
    TEST={
        "API": "https://testnet.binancefuture.com",
        "WEBSOCKET": "wss://stream.binancefuture.com",
    },
)
