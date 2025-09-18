import websockets
import json
import uuid
import asyncio
from websockets.asyncio.client import connect

def create_websocket_client():
    return connect("ws://localhost:8085")

async def authenticate(ws):
    await ws.send(json.dumps({
        "id": str(uuid.uuid4()), 
        "method": "authenticateWithPassword", 
        "params": {"username": "admin", "password": "admin"}
    }))
    auth_response = json.loads(await ws.recv())

    # token = response["result"]["token"]
    # {'jsonrpc': '2.0', 'id': '6c91f773-ba11-42ad-9cf8-bd860d94e5fb', 'result': {'token': '29de64ef-29f6-49c1-9fa3-6aa815bb9c49', 'user': {'id': 'admin', 'name': 'Admin', 'language': 'DE', 'hasMultipleEdges': False, 'settings': {}, 'globalRole': 'admin'}
    user = auth_response["result"]["user"]

    assert user["id"] == "admin"
    assert user["globalRole"] == "admin"