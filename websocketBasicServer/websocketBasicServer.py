#/usr/bin/env python
# websocketBasicServer.py

import asyncio
import websockets
import serial
import time
import json

ser = serial.Serial('/dev/ttyACM0', 9600)

connected = set()

data = {}

async def sendSerialNumber():
	while True:
		if ser.isOpen():
			ser.write('B{}/n'.format('3').encode())
			print("3")
			await asyncio.sleep(1)
			ser.write('B{}/n'.format('3').encode())
			print("2")
			await asyncio.sleep(1)
		else:
			print("opening error")
			await asyncio.sleep(2)

async def sendSerialJson():
	while True:
		if ser.isOpen():
			data["test"] = 1
			joyData = json.dumps(data)
			ser.write(joyData.encode('ascii'))
			ser.flush() # Wait until information is sent before moving on.. I think?
			try:    # Try to do this, if not run Exception code (Print error message)
				incoming = ser.readline().decode("utf-8")
				print(incoming)
			except Exception as e:
				print (e)
				pass
			#ser.close()   # In original code, not sure I need. 
			await asyncio.sleep(1)
		else:
			print("opening error")
			await asyncio.sleep(2)	

async def websocketJoystick(websocket, path):
	connected.add(websocket)
	while True:
			info  = await websocket.recv()
			#ser.write('{}\n'.format(info).encode())
			#print(f"recieved: {info}")
			data.clear()
			try:
				data.update(json.loads(info))
			except json.decoder.JSONDecodeError as e:
				print(e)
				pass
			print(data["Axis 0"])
			await asyncio.wait([ws.send(info) for ws in connected])
			await asyncio.sleep(0.5)

async def joystickGet():
	server = await websockets.serve(websocketJoystick, "0.0.0.0", 8765)
	await server.wait_closed() 


loop = asyncio.get_event_loop()
get = loop.create_task(joystickGet())
send = loop.create_task(sendSerialJson())

loop.run_forever()


#async def main():
#	#send = asyncio.create_task(sendSerialJson())
#	receive = asyncio.create_task(joystickGet()) #create_task automagically makes the task run soon. 
	
#if __name__ == "__main__":
#	while True:
#		asyncio.run(main())
	
	#	if ser.isOpen():
	#		line = ser.readline()
	#		print(line)
	

#asyncio.get_event_loop().run_until_complete(server)
#asyncio.get_event_loop().run_forever()
