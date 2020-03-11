
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1:
	ser.write(1500)
	time.sleep(2)
	for x in range ('1500','1900'):
		ser.write(x)
		time.sleep(0.1)
	for x in range ('1900', '1500'):
		ser.write(x)
		time.sleep(0.1)
	for x in range ('1500', '1100'):
		ser.write(x)
		time.sleep(0.1)
	for x in range ('1100', '1500'):
		ser.write(x)
		time.sleep(0.1)
		
		
