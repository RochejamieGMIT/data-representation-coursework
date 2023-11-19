import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jr200195"
)

mycursor = db.cursor()

# Example: Fetching data from a table
#sql = "SELECT * FROM test"
mycursor.execute("create DATABASE Datarep")


mycursor.close()
db.close()