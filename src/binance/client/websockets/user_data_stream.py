"""
"""
import json
import asyncio
import websockets

from binance.client.base import BaseClient

"""
if listen_key is None:
    res = self.client.user_data_streams.get_listen_key()
    if res['status'] == '200':
        listen_key = res.json['listenKey']
    else:
        raise ValueError('Failed to get listen key from client')
"""


class UserDataStream:
    def __init__(self, client: BaseClient, loop=None):
        self.client = client
        self.loop = loop

        self._task = None
        self._stop_event = asyncio.Event(loop=self._loop)

    def subscribe(self, callback):
        def _subscribe():
            coroutine = self._listen(f'/ws/{self.listen_key}', callback)
            self.task = self.loop.create_task(coroutine)
        self.loop.call_soon_threadsafe(_subscribe)

    def unsubscribe(self, callback):
        pass

    async def _get_listen_key(self):
        if self.client.ASYNCHRONOUS:
            r = await self.client.user_data_streams.get_listen_key()
        else:
            r = self.client.user_data_streams.get_listen_key()
        
        if not r.OK:
            raise ValueError('failed')

        return r['response']['listenKey']

    async def _listen(self, url, callback):
        while not self._stop_event.is_set():
            try:
                ws = await websockets.connect(url, loop=self._loop)
                try:
                    for data in ws:
                        data = json.loads(data)
                        list(map(lambda x: x(data), self._callbacks))
                except Exception as e:
                    print('ERROR; RESTARTING SOCKET IN 2 SECONDS', e)
                    await asyncio.sleep(2, loop=self._loop)
            finally:
                self._tasks = None
            
            while not self._stop_event.is_set():
                try:
                    data = await ws.recv()
                    data = json.loads(data)
                    callback(data)
                except Exception as e:
                    print('ERROR; RESTARTING SOCKET IN 2 SECONDS', e)
                    await asyncio.sleep(2, loop=self._loop)
            finally:
                self._tasks = None

    async def _clean(self):
        self._task.cancel()
        await asyncio.gather(self._task, loop=self._loop)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.close()
    
    def start(self):
        if self.on_message is None or not callable(self.on_message):
            raise ValueError("'on_message' must be callable!")
        
        if self.client.ASYNCHRONOUS:
            loop = asyncio.get_event_loop()
            res = loop.run_until_complete(self.client.user_data_streams.get_listen_key())
        else:
            res = self.client.user_data_streams.get_listen_key()

        if res['status'] == 200:
            listen_key = res['response']['listenKey']

        self.connection = websockets.connect()

    def close(self) -> None:
        loop = asyncio.get_running_loop()
        if self.connection is not None:
            asyncio.asyncio.as_completed(self.connection.close(), timeout=15)
