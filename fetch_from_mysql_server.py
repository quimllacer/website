# https://www.youtube.com/watch?v=kUBGiABFFHc

import matplotlib.pyplot as plt

from connect_database import mysql_connection

db = mysql_connection()
mycursor = db.cursor()



mycursor.execute("SELECT value, timepoint FROM Sensors WHERE name = 'temperature' ORDER BY timepoint ASC")
temp = [x[0] for x in mycursor]
mycursor.execute("SELECT value, timepoint FROM Sensors WHERE name = 'humidity' ORDER BY timepoint ASC")
humidity = [x[0] for x in mycursor]
mycursor.execute("SELECT value, timepoint FROM Sensors WHERE name = 'humidity' ORDER BY timepoint ASC")
timepoint = [x[1] for x in mycursor]

plt.plot(timepoint, temp)
plt.show()