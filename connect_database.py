# https://www.youtube.com/watch?v=91iNR0eG8kE

import mysql.connector

def mysql_connection():
    db = mysql.connector.connect(
        host = "sql224.main-hosting.eu",
        user = "u747198295_root",
        passwd = "Soydel1996",
        database = "u747198295_mydatabase"
        )
    return db

if __name__ == '__main__':
    mycursor = db.cursor()

    # Create a table with spceific columns
    # mycursor.execute("CREATE TABLE Sensors (name varchar(50) NOT NULL, value float NOT NULL, timepoint datetime NOT NULL, sensorID int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

