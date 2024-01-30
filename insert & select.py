import mysql.connector as mycon

mydb = mycon.connect(host="localhost", user="root", password="12345678", database="Ashish7")

dbc = mydb.cursor()

   # ------------ VIEWING DATA ------------

db_select = dbc.execute("select* from Ashish7.friends")

db_select = dbc.fetchall()
print(db_select)


       # --------- INSERTING DATA ---------
# dbinsert = "INSERT INTO friends(roll, name, class) VALUES (%s, %s, %s)"

# dbvalue = [(4, "Vishal", 14), (5, "Satyam", 11), (6, "Himanshu", 16)]

# dbc.executemany(dbinsert, dbvalue)
# mydb.commit()

# print("Data Inserted")


