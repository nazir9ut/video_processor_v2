from peewee import *
import datetime

zm_db = MySQLDatabase(
    'zm',  # Required by Peewee.
    user='root',  # Will be passed directly to psycopg2.
    password='z',  # Ditto.
    host='127.0.0.1',  # Ditto.
)



class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = zm_db

class Events(BaseModel):
    class Meta:
        db_table = 'Events'



ev = Events.select()

print(ev[0].id)