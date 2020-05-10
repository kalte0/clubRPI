#!/usr/bin/env python
# WS server example

import asyncio
import websockets
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

connected = set()

async def hello(websocket, path):
	connected.add(websocket)
	while True:
			name = await websocket.recv()
			#ser.write(b'A128\n')
			ser.write('{}\n'.format(name).encode())
			
			print(f"< {name}")

			greeting = f"Hail and well met, {name}!"

			# await websocket.send(greeting)
			await asyncio.wait([ws.send(greeting) for ws in connected])
			print(f"> {greeting}")

start_server = websockets.serve(hello, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
