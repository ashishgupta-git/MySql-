import mysql.connector as mycon

mydb = mycon.connect(host="localhost", user="root", password="12345678", database="Ashish7")

dbc = mydb.cursor()

db_select = dbc.execute("show tables")

db_select = dbc.fetchall()
print(db_select)


# dbinsert = "INSERT INTO friends(roll, name, class) VALUES (%s, %s, %s)"

# dbvalue = [(1, "Ashish", 12), (2, "Rohan", 10), (2, "Phoolchand", 14)]

# dbc.executemany(dbinsert, dbvalue)
# mydb.commit()

# print("Data Inserted")


