import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "datarep"
)

mycursor = db.cursor()

sql = "update student set name= %s, age= %s where id =%s"
values = ("Clod",28,2)
# Example: Fetching data from a table
#sql = "SELECT * FROM test"
mycursor.execute(sql,values)
db.commit()
print("Updated Record")

mycursor.close()
db.close()