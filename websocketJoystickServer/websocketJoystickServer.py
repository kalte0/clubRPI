
import asyncio
import websockets
import serial
import time


async def hello(websocket, path):
	while True:
			num = await websocket.recv()
			
			print(f"< {num}")
			greeting = f"Hello {num}!"
			await websocket.send(greeting)
			print(f"> {greeting}")

start_server = websockets.serve(hello, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
