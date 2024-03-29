from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
import os

import models

from api.user import user
from api.blog import blog

DEBUG = True
PORT = 8000

login_manager = LoginManager()

app = Flask(__name__, static_url_path="", static_folder="static")

app.secret_key="secret secret are no fun, secret secret hurt someone lol"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

CORS(user, origins=['http://localhost:3000', 'https://boiling-mountain-12693.herokuapp.com'], supports_credentials=True)
CORS(blog, origins=['http://localhost:3000', 'https://boiling-mountain-12693.herokuapp.com'], supports_credentials=True)

app.register_blueprint(user)
app.register_blueprint(blog)

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return "feelings server lol"

if 'ON_HEROKU' in os.environ:
    print('hitting ')
    models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)