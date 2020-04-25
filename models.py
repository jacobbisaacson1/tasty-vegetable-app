# print('importing correctly from models.py')

from peewee import *
import datetime

DATABASE = SqliteDatabase('vegs.sqlite')


class Veg(Model):
	name = CharField()
	color = CharField()
	isTasty = Boolean()
	created_at: DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Veg], safe=True)
  print("--- CONNECTED TO DB AND CREATED TABLES IF THEY WEREN'T ALREADY THERE ---")

  DATABASE.close()







