
from flask import Flask, request, url_for, redirect

app = Flask(__name__)

# decorator


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
    return redirect(url_for('post', post_id=2))

    
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    # return 'Hello please sign up '
