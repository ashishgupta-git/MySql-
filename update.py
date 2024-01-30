import mysql.connector as mycon

mydb = mycon.connect(host="localhost", user="root", password="12345678", database="Ashish7")

dbc = mydb.cursor()

dbupdate = "update Ashish7.friends set class=%s where name=%s"

dbvalue = (15,"himanshu")

dbc.execute(dbupdate,dbvalue)

mydb.commit()

print("Data Updated....")