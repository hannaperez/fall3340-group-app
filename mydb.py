import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'flq0AP..',
	)

#prepare cursor object (using the connector declare above)
cursorObject = dataBase.cursor() 

#create data base
cursorObject.execute("CREATE DATABASE 3340data")

#Message in console to see if it worked 
print("Hello data base 3340data")
