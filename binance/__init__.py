"""
Binance API
"""
from binance import order
from binance.client.aioclient import AIOClient
from binance.client.client import Client

from .version import __version__

__all__ = ["Client", "AIOClient", "order", __version__]
