
import mysql.connector

# connect to the database
# return instance of sql
mydb = mysql.connector.connect(
    host='localhost',
    user='savecode',
    password='0986778998Salva!',
    database='sql_test',
)

# cursor is object with the following
# of the db

cursor = mydb.cursor()

cursor.execute('select * from Persons')


data = cursor.fetchall()

print(data)