#!/usr/bin/env python3.8
import aiohttp
import asyncio

class Client(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self._session = aiohttp.ClientSession()

