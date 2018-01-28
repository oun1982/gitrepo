__author__ = 'oun1982'

import mysql.connector


conn = mysql.connector.connect(user='root',password='',host='localhost',database='beagle')
mycursor = conn.cursor()
mycursor.execute("SELECT * FROM agents")
row = mycursor.fetchone()
while row is not None:
    print(row)
    row = mycursor.fetchone()
print("Number of Rows :",mycursor.rowcount)
conn.close