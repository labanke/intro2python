from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Laban.db"))

#creating table inside db
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
User.create_table(fail_silently=True)

class Student(Model):
    name = CharField()
    phoneno = IntegerField()
    age = IntegerField()
    gender = CharField()
    studentcode = IntegerField(unique=True)

    class Meta:
        database = db
Student.create_table(fail_silently=True)