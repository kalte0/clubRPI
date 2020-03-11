import serial
import time

count = 0 
ser = serial.Serial('/dev/ttyACM0', 9600)

ser.write('1');
time.sleep(5); 

while 1:
    ser.write('1')
    time.sleep(2)
    ser.write('0')
    time.sleep(2)
    ser.write('1')
    time.sleep(2)
    ser.write('2')
    time.sleep(2)


