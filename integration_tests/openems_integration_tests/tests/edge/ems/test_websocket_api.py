from openems_integration_tests.ems.ems import EmsClient, EmsState
from openems_integration_tests.ems.websocket_util import *
from openems_integration_tests.ems.websocket_client import *
import websocket
import json
import uuid
import asyncio

# def test_websocket_reachable(ems_cli: EmsClient):
#     ws = create_websocket_client()
#     authenticate(ws)

# def test_websocket_get_edge_config(ems_cli: EmsClient):
#     ws = create_websocket_client()
#     authenticate(ws)
    
#     ws.send(json.dumps({
#         "id": str(uuid.uuid4()), 
#         "method": "edgeRpc", 
#         "params": {
#             "edgeId": "edge0",
#             "payload": {
#         "id": str(uuid.uuid4()), 
#         "method": "getEdgeConfig", 
#         "params": {}
#     }
#         }
#     }))
#     response = json.loads(ws.recv())
#     edge_config = response["result"]["payload"]["result"]
#     # {'components': {'_appManager': {'alias': 'Core.AppManager', 'factoryId': 'Core.AppManager', 'properties': {'apps': '[]', 'keyForFreeApps': '0000-0000-0000-0000'}}, '_componentMana
#     assert "components" in edge_config

def test_websocket(ems_cli: EmsClient):
    async def run():
        ws = await create_websocket_client("ws://localhost:8085")
        ws.authenticate()

    asyncio.run(run())



# def test_websocket_subscribe_channels(ems_cli: EmsClient):

#     async def run():
#         async with connect("ws://localhost:8085") as ws:
#             await authenticate(ws)
    
#             async def get_value_from_subscribed_channel(channel: str, max_tries: int = 5) -> int:
                
#                 await ws.send(json.dumps({
#                     "id": str(uuid.uuid4()), 
#                     "method": "edgeRpc", 
#                     "params": {
#                         "edgeId": "edge0",
#                         "payload": {
#                             "id": str(uuid.uuid4()), 
#                             "method": "subscribeChannels", 
#                             "params": {
#                                 "count": 1,
#                                 "channels": [channel]
#                             }
#                         }
#                     }
#                 }))

#                 counter = 0
#                 while True:
#                     try:
#                         # Wait for a message with a 1 second timeout
#                         response = await asyncio.wait_for(ws.recv(), timeout=1.0)
#                         print("Received:", response)
#                         # raise Exception(json.loads(response))
#                         if response is None:
#                             continue
#                         counter += 1
#                         if counter >= max_tries:
#                             raise Exception(response)
#                         parsed = json.loads(response)  
#                          # {"jsonrpc":"2.0","method":"edgeRpc","params":{"edgeId":"0","payload":{"jsonrpc":"2.0","method":"currentData","params":{"_sum/State":0}}}}
#                         if "params" in parsed and parsed["params"]["payload"]["method"] == "currentData":
#                             return parsed["params"]["payload"]["params"][channel]
#                     except asyncio.TimeoutError:
#                         # Triggered every second if no message was received
#                         print("No message this second")
                            
#             async def update_component(component_id: str, properties: dict):
#                 await ws.send(json.dumps({
#                     "id": str(uuid.uuid4()),
#                     "method": "edgeRpc",
#                     "params": {
#                         "edgeId": "edge0",
#                         "payload": {
#                             "id": str(uuid.uuid4()),
#                             "method": "componentJsonApi",
#                             "params": {
#                                 "componentId": "_componentManager",
#                                 "payload": {
#                                     "id": str(uuid.uuid4()),
#                                     "method": "updateComponentConfig",
#                                     "params": {
#                                         "componentId": component_id,
#                                         "properties": properties,
#                                     }
#                                 }
#                             }
#                         }
#                     }
#                 }))
#                 return await asyncio.wait_for(ws.recv(), timeout=5.0)
            

#             sumState = await get_value_from_subscribed_channel("_sum/State")
#             assert sumState == EmsState.OK.value

#             a = await update_component("_appManager", [{"name": "keyForFreeApps", "value": "0000-0001-1000-0000"}])
#             raise Exception(a)



#     asyncio.run(run())