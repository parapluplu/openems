from openems_integration_tests.ems.ems import EmsClient, EmsState
from openems_integration_tests.ems.websocket_util import *
import websocket
import json
import uuid

def test_websocket_reachable(ems_cli: EmsClient):
    ws = create_websocket_client()
    authenticate(ws)

def test_websocket_reachable(ems_cli: EmsClient):
    ws = create_websocket_client()
    authenticate(ws)
    
    ws.send(json.dumps({
        "id": str(uuid.uuid4()), 
        "method": "edgeRpc", 
        "params": {
            "edgeId": "edge0",
            "payload": {
        "id": str(uuid.uuid4()), 
        "method": "getEdgeConfig", 
        "params": {}
    }
        }
    }))
    response = json.loads(ws.recv())
    edge_config = response["result"]["payload"]["result"]
    assert "components" in edge_config

