"""
"""
import asyncio
import json
import logging
from asyncio import CancelledError

from binance.client.base import BaseClient

log = logging.getLogger(__file__)


class UserDataStream:
    def __init__(self, client: BaseClient, loop=None):
        self.client = client
        self.loop = loop

        self._callbacks = list()
        self._listener_task = None

    def subscribe(self, callback):
        def _subscribe():
            log.debug("Add callback {callback}.")
            self._callbacks.append(callback)
            if self._listener_task is None:
                self._listener_task = self.loop.create_task(self._listener())

        self.loop.call_soon_threadsafe(_subscribe)

    def unsubscribe(self, callback=None):
        def _unsubscribe(self):
            log.debug("Remove callback {callback}")
            self._callbacks.remove(callback)
            if not self._callbacks:
                self._ws_task.cancel("No more callbacks")

        self.loop.call_soon_threadsafe(_unsubscribe)

    async def _keep_listen_key_alive(self):
        if self.client.ASYNCHRONOUS:
            r = await self.client.user_data.keep_listen_key_alive()
        else:
            r = self.client.user_data.keep_listen_key_alive()
        if not r.OK:
            raise ValueError("failed")

    async def _get_listen_key(self):
        if self.client.ASYNCHRONOUS:
            r = await self.client.user_data.get_listen_key()
        else:
            r = self.client.user_data.get_listen_key()
        if not r.OK:
            raise ValueError("failed")
        return r["response"]["listenKey"]

    async def _listener(self):
        async def keep_alive(self):
            while True:
                await asyncio.sleep(60 * 50)
                await self._keep_listen_key_alive()

        keep_alive_task = self.loop.create_task(keep_alive())
        try:
            while True:
                listen_key = await self._get_listen_key()
                url = f"{self.client._websocket_base}/ws/{listen_key}"
                try:
                    ws = await websockets.connect(url, loop=self.loop)
                    for data in ws:
                        data = json.loads(data)
                        list(map(lambda x: x(data), self._callbacks))
                except ConnectionClosed as e:
                    log.error(f"Connection closed; {e}. Restarting socket.")
                finally:
                    ws.close()
        except CancelledError:
            log.debug("CancelledError raised in _listener(); {e}.")
        finally:
            keep_alive_task.cancel()
            self._listener_task = None

    async def _clean(self):
        self._task.cancel()
        await asyncio.gather(self._task, loop=self._loop)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def close(self) -> None:
        self._ws_task.cancel()
