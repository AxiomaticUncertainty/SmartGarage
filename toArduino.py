from serial import Serial
import time

ser = Serial("COM4", 9600)
x = ser.readline()
print(x)
# time.sleep(1)
ser.write(("a").encode('raw_unicode_escape'))
x = ser.readline()
print(x)
# ser.write(("test").encode('raw_unicode_escape'))
# x = ser.readline()
# print(x)
