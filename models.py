from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('vegs.sqlite')


class Veg(Model):
	name = CharField()
	color = CharField()
	isTasty = CharField()
	created_at: DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class User(UserMixin, Model):
  username=CharField(unique=True)
  email=CharField(unique=True)
  password=CharField()

  class Meta:
    database = DATABASE


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, Veg], safe=True)
  print("--- CONNECTED TO DB AND CREATED TABLES IF THEY WEREN'T ALREADY THERE ---")

  DATABASE.close()







