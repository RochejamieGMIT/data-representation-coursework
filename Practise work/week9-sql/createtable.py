import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "datarep"
)

mycursor = db.cursor()

sql = "create table Test2 (id int auto_increment primary key, name varchar(250), age int)"
# Example: Fetching data from a table
#sql = "SELECT * FROM test"
mycursor.execute(sql)


mycursor.close()
db.close()