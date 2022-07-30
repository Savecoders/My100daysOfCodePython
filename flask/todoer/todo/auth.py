
# ? functools is a set of functions that can be used

from contextlib import redirect_stderr
from distutils.log import error
import functools

from flask import (
    Blueprint, flash, g, render_template, request, url_for,
    session, redirect
)

# * blueprints is package of modules
# * flask is a function of send messages in templates

from werkzeug.security import check_password_hash, generate_password_hash

# * incrypt a password use hash algorithm

from todo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# using the blueprint and not using app


@bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        db = get_db()
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'select is from user where username = %s'
        )

        if not username:
            error = 'Username must be specified'

        if not password:
            error = 'Password must be specified'
        elif c.fetchone() is not None:
            error = "User already exists"

        if error is None:
            c.execute(
                'insert into user (username, password) values (%s, %s)',
                (username, generate_password_hash(password))
            )
            c.commit()

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'select * from user where username = %s', (username)
        )

        user = c.fetchone()

        if user is None:
            error = 'Invalid password or username'
        elif not check_password_hash(user['password'], password):
            error = 'Invalid password or username'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        flash(error)

    return render_template('auth/login.html')
