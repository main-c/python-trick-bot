from peewee import *

database = SqliteDatabase('bot.db')

class BaseModel(Model):
    class Meta:
        database = database

class Trick(BaseModel):
    platform = CharField()
    title = CharField()
    link = CharField(unique=True)
    content = TextField()
	
database.create_tables([Trick])