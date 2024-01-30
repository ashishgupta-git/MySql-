import mysql.connector as mycon

mydb = mycon.connect(host="localhost", user="root", password="12345678")

print(mydb, "Connection Sucessfull...")