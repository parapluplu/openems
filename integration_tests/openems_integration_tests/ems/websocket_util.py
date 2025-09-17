import websocket
import json
import uuid

def create_websocket_client() -> websocket.WebSocket:
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8085")
    return ws

def authenticate(ws: websocket.WebSocket):
    ws.send(json.dumps({
        "id": str(uuid.uuid4()), 
        "method": "authenticateWithPassword", 
        "params": {"username": "admin", "password": "admin"}
    }))
    auth_response = json.loads(ws.recv())

    user = auth_response["result"]["user"]

    assert user["id"] == "admin"
    assert user["globalRole"] == "admin"