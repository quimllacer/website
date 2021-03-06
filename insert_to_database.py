import re
import serial
from datetime import datetime

from connect_database import mysql_connection



ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()
while True:
    if ser.in_waiting > 0:
        try:
            db = mysql_connection()
            mycursor = db.cursor()
            
            line = ser.readline().decode('utf-8').rstrip()
            vals = [float(s) for s in re.findall(r'-?\d+\.?\d*', line)] # Use regex to extract the values from the string.
            vals.append(datetime.now())
            humidity = vals[0]
            temperature = vals[1]
            timepoint = vals[2]
            mycursor.execute("INSERT INTO Sensors (name, value, timepoint) VALUES (%s, %s, %s)", ("humidity", humidity, timepoint))
            mycursor.execute("INSERT INTO Sensors (name, value, timepoint) VALUES (%s, %s, %s)", ("temperature", temperature, timepoint))
            db.commit()
            print(humidity, temperature, timepoint)
        except Exception as e: print(e)
            
