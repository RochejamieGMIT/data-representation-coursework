import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "datarep"
)

mycursor = db.cursor()

sql = "insert into student (name,age) values (%s,%s)"
values = ("Jamie",28)
# Example: Fetching data from a table
#sql = "SELECT * FROM test"
mycursor.execute(sql,values)
db.commit()
print("1 record inserted, ID: ", mycursor.lastrowid)

mycursor.close()
db.close()