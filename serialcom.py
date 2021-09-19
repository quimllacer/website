import re
import serial
from datetime import datetime
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            vals = [float(s) for s in re.findall(r'-?\d+\.?\d*', line)] # Use regex to extract the values from the string.
            vals.append(datetime.now())
            humidity = vals[0]
            temperature = vals[1]
            time_point = vals[2]
            print(humidity, temperature, time_point)