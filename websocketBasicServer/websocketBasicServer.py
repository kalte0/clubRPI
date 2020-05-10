#!/usr/bin/env python
# websocketBasicServer.py

import asyncio
import websockets
import serial
import time
import json

ser = serial.Serial('/dev/ttyACM0', 9600)

connected = set()

async def sendSerial():
	while True:
		if ser.isOpen():
			ser.write(3)
			print("3")
			await asyncio.sleep(1)
			ser.write(2)
			print("2")
			await asyncio.sleep(1)
		else:
			print("opening error")
			await asyncio.sleep(2)

async def websocketJoystick(websocket, path):
	connected.add(websocket)
	while True:
			info  = await websocket.recv()
			#ser.write(b'A128\n')
			ser.write('{}\n'.format(info).encode())

			print(f"recieved: {info}")

			# returnInfo = info

			# await websocket.send(returnInfo)
			await asyncio.wait([ws.send(info) for ws in connected])
			#print(f"> {greeting}")
            
			await asyncio.sleep(0.5)

async def joystickGet():
	server = await websockets.serve(websocketJoystick, "0.0.0.0", 8765)
	await server.wait_closed() 
	
if __name__ == "__main__":
	while True:
		asyncio.run(sendSerial())
		asyncio.run(joystickGet())

#asyncio.get_event_loop().run_until_complete(server)
#asyncio.get_event_loop().run_forever()
