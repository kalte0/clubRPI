import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

connected = set()

print("3");

while True:
	if ser.isOpen():
		line = ser.readline()
		print(line)
