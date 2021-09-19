# https://www.youtube.com/watch?v=91iNR0eG8kE

import mysql.connector

db = mysql.connector.connect(
	host = "sql224.main-hosting.eu",
	user = "u747198295_root",
	passwd = "Soydel1996",
	database = "u747198295_mydatabase"
	)

mycursor = db.cursor()

# Create a table with spceific columns
# mycursor.execute("CREATE TABLE Sensors (name varchar(50) NOT NULL, value float NOT NULL, timepoint datetime NOT NULL, sensorID int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Sensors (name, value, tstamp) VALUES (%s, %s, %s)", ("temperature, 25, tstamp"))
mycursor.execute("DESCRIBE Sensors")

for x in mycursor:
	print(x)
