import mysql.connector as mycon

mydb = mycon.connect(host="localhost", user="root", password="12345678")

dbc = mydb.cursor()

dbc.execute("create database Ashish7")

print("Database Created...")