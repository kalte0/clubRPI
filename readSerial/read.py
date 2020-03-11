import serial
import time

count = 0
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1: 
    count+=1
    ser.write('{:d}\n'.format(count))
    time.sleep(.5)
    #line = ser.readline()
    #print(line)
