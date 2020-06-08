import asyncio
import websockets
import serial
import time


async def coroutineOne(): 
	x = 1
	while (x < 10):
		await asyncio.sleep(1)
		print(x)
		x += 1

async def coroutineTwo():
	x = 10
	while (x > 1):
		await asyncio.sleep(0.5)
		print(x)
		x -= 1
		
loop = asyncio.get_event_loop()
one = loop.create_task(coroutineOne())
two = loop.create_task(coroutineTwo())

try:
	loop.run_until_complete(two)
except asyncio.CancelledError:
	pass


#if __name__ == "__main__":
#	asyncio.run(main())
