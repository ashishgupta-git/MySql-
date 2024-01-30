import mysql.connector as mycon

mydb = mycon.connect(host="localhost", user="root", password="12345678", database="Ashish7")

dbc = mydb.cursor()

dbc.execute("create table Gfs(roll int, name varchar(20), class int)")

print("Table Created...")

# for i in dbc:
#     print(i)



