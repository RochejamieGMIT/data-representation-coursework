import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "datarep"
)

mycursor = db.cursor()

sql = "delete from student where id =%s"
values = (2,)
# Example: Fetching data from a table
#sql = "SELECT * FROM test"
mycursor.execute(sql,values)
db.commit()
print("deletion Done")

mycursor.close()
db.close()