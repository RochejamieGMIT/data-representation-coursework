import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jr200195",
    database = "datarep"
)

mycursor = db.cursor()

sql = "select * from student where id = %s;"
values = (1,)
# Example: Fetching data from a table
#sql = "SELECT * FROM test"
mycursor.execute(sql,values)
result = mycursor.fetchall()
for x in result:
    print(x)

mycursor.close()
db.close()