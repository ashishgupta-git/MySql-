import mysql.connector as mycon

mydb = mycon.connect(host="localhost", user="root", password="12345678")

dbc = mydb.cursor()

delete_all = "truncate table Ashish7.friends"

dbc.execute(delete_all)

mydb.commit()

print("All Record Deleted....!")


# db_delete_data = "delete from Ashish7.friends where name=%s"

# dbvalue = ("Himanshu",)

# dbc.execute(db_delete_data,dbvalue)

# mydb.commit()

# print("Record Deleted.....")