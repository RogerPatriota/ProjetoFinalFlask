from flask import Flask
from .routes.ucBp import ucBp 
from .extensions import db, migrate

'''
$env:FLASK_APP = "ProjetoFinalFlask"
$env:FLASK_ENV = "development"
'''

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(ucBp)

    return app