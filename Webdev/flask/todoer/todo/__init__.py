import os
from flask import Flask


def create_app():
    
    app = Flask(
        __name__,
        static_url_path='',
        static_folder='public/static',
        template_folder='public/templates'
    )

    app.config.from_mapping(
        SECRET_KEY='mykey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    # generate blueprint
    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route('/message')
    def message():
        return 'Hello World!'

    return app
