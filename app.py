from flask import Flask, g

import models

DEBUG = True
PORT = 8000

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)