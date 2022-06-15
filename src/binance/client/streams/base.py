import logging
import asyncio
import random

log = logging.getLogger(__file__)

PENDING = 'PENDING'
CONNECTING = 'CONNECTING'
LISTENING = 'LISTENING'
DISCONNECTED = 'DISCONNECTED'

class BinanceStream(asyncio.Protocol):
    max_delay = 3600
    initial_delay = 1.0
    factor = 2.7182818284590451
    jitter = 0.119626565582
    max_retries = None

    def __init__(self, *args, loop=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.loop = loop
        self._args = args
        self._kwargs = kwargs

        self._retries = 0
        self._delay = self.initial_delay
        self._continue_trying = True
        self._call_handle = None
        self._connector = None
        self.state = PENDING

    def connection_lost(self, exc):
        log.debug(f'Connection lost with exception: {exc}')
        if self._continue_trying:
            self._retry()

    def connection_failed(self, exc):
        log.debug(f'Connection failed with exception: {exc}')
        if self._continue_trying:
            self._retry()

    def _retry(self):
        if not self._continue_trying:
            return

        self._retries += 1
        if self.max_retries is not None and (self._retries > self.max_retries):
            return

        self._delay = min(self._delay * self.factor, self.max_delay)
        if self.jitter:
            self._delay = random.normalvariate(self._delay,
                                               self._delay * self.jitter)
        self._call_handle = self.loop.call_later(self._delay, self.connect)

    def connect(self):
        if self._connector is None:
            self._connector = self.loop.create_task(self._connect())

    async def _connect(self):
        try:
            await self.loop.create_connection(lambda: self, *self._args, **self._kwargs)
        except Exception as exc:
            self.loop.call_soon(self.connection_failed, exc)
        finally:
            self._connector = None

    def disconnect(self):
        pass
        
    def stop_trying(self):
        if self._call_handle:
            self._call_handle.cancel()
            self._call_handle = None
        self._continue_trying = False
        if self._connector:
            self._connector.cancel()
            self._connector = None



class BinanceStreams:
    factory = None

    def __init__(self, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.loop = loop

    def connect(self):
        pass
    
    async def connect(self, url, callbacks):
        transport, protocol = self.loop.create_connection(self.factory, url, 8888)
        self.task = self.loop.create_task(coro)


        