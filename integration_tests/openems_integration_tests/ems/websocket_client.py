from websockets.asyncio.client import connect
import asyncio
import threading
import uuid
import json


async def create_websocket_client(uri: str):
    r = await connect(uri)
    raise Exception(type(r))
    return WebsocketClient(r)

class WebsocketClient(object):
    _requests: dict[str, asyncio.Future] = {}

    def __init__(self, websocket):
        self.websocket = websocket
        
        loop = asyncio.get_event_loop()
        loop.create_task(self._debug_loop())
        loop.run_forever()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.websocket.close()
    
    async def _debug_loop(self):
        while True:
            message = await self.websocket.recv()
            self._on_message(message)

    def _on_message(self, message):
        data = json.loads(message)
        request_id = data.get("id")
        if request_id and request_id in self._requests:
            future = self._requests.pop(request_id)
            if not future.done():
                future.set_result(data)
        print(message)

    async def request(self, method: str, params: dict):
        request_id = str(uuid.uuid4())
        future = asyncio.get_event_loop().create_future()
        self._requests[request_id] = future

        await self.websocket.send(json.dumps({
            "id": request_id,
            "method": method,
            "params": params
        }))
        
        return await future

    async def authenticate(self):
        response = await self.request("authenticateWithPassword",  {"username": "admin", "password": "admin"})
        
        # {'jsonrpc': '2.0', 'id': '6c91f773-ba11-42ad-9cf8-bd860d94e5fb', 'result': {'token': '29de64ef-29f6-49c1-9fa3-6aa815bb9c49', 'user': {'id': 'admin', 'name': 'Admin', 'language': 'DE', 'hasMultipleEdges': False, 'settings': {}, 'globalRole': 'admin'}
        token = response["result"]["token"]
        user = response["result"]["user"]
