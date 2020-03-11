
import asyncio
import websockets
import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)

connected = set()

async def hello(websocket, path):
	while True:
			name = await websocket.recv()
			print(f"< {name}")
			#ser.write('{}\n'.format(name).encode())

			greeting = f"Hello {name}!"

			await websocket.send(greeting)
			#await asyncio.wait([ws.send(greeting) for ws in connected]) #Same as above, but does procedure
					#for all connected devices. 
			print(f"> {greeting}")

start_server = websockets.serve(hello, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
