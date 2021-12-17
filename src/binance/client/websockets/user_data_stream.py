"""
"""
import asyncio
import websockets

class UserDataStream:
    def __init__(self, client, on_message = None):
        self.client = client
        self.on_message = on_message
        self.connection = None

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
