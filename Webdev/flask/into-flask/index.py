
import mysql.connector
from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

# decorator


# connect to the database
# return instance of sql
mydb = mysql.connector.connect(
    host='localhost',
    user='savecode',
    password='0986778998Salva!',
    database='sql_test',
)


# enable dictionary mode
# for default settings is tuples

cursor = mydb.cursor(dictionary=True)

@app.route('/')
def index():
    return 'Hello Worlds!'

# methods GET POST PUT DELETE

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    if request.method == 'GET':
        return 'the id of the post is: ' + post_id
    else:
        return 'Get id: ' + post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    cursor.execute('select * from Persons')
    users = cursor.fetchall()
    print(users)
    # management permissions
    # abort(403)
    # return redirect(url_for('post', post_id=2))
    # return render_template('login.html')

    return render_template('login.html', users=users)
    
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    # return 'Hello please sign up '


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hello word')


@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        sql = "insert into Persons (username,email) values (%s, %s)"
        values = (username, email)
        cursor.execute(sql, values)
        # save the user
        mydb.commit()

        return redirect(url_for('login'))

    return render_template('sign.html')