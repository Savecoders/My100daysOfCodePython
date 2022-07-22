
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

#? show elements from Persons
# select the table from Persons
cursor.execute('select * from Persons limit 1')

# show the columns from the table
# cursor.execute('show create table Persons')

#? insert data from the Table

# sql = 'insert into Persons (username,email) values (%s, %s)'
# values = ('Savecoders','myaddress@email.com')

#? update data

# sql = 'update Persons set email = %s where email = %s'
# values = ('testsql@gmail.com', 'Salvador75WF@gmail.com')
# cursor.execute(sql, values)

#? delete data from the Table

# sql = 'delete from Persons where UserName = %s'
# later the first element of tuple, add the ','
# values = ('Savecoders',)

# cursor.execute(sql, values)


#* save changes to the database
# mydb.commit()

# fetchall return all the instances of sql
# fetchone return the first instance of sql
data = cursor.fetchall()

print(data)