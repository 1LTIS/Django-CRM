import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'debilas',

	)

corsorObject = dataBase.cursor()

corsorObject.execute("CREATE DATABASE elderco2")

print("All Done")