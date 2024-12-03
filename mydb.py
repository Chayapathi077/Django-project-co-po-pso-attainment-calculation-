import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '9980890064p*',

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE 3ps")

print("All Done!")