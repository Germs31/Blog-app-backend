from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('blogs.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    image = CharField()

    class Meta:
        database = DATABASE

class Blog(Model):
    title = CharField()
    author = CharField()
    text = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Blog], safe=True)
    print("Created Tables")
    DATABASE.close()