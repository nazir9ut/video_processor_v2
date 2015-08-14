from peewee import *
import datetime
import json


db = MySQLDatabase(
    'zm',  # Required by Peewee.
    user='root',  # Will be passed directly to psycopg2.
    password='z',  # Ditto.
    host='127.0.0.1',  # Ditto.
)



class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db


    def __str__(self):
        r = {}
        for k in self._data.keys():
          try:
             r[k] = str(getattr(self, k))
          except:
             r[k] = json.dumps(getattr(self, k))
        return str(r)



class Monitor(BaseModel):
    class Meta:
        db_table = 'Monitors'

    name = CharField(max_length=64, db_column = "Name")





class Event(BaseModel):
    class Meta:
        db_table = 'Events'

    monitor_id = IntegerField(db_column = "MonitorId")
    cause = CharField(db_column = "Cause")
    length = DecimalField(db_column = "Length")
    start_time = DateTimeField(db_column = "StartTime")






class PrVideo(BaseModel):
    path_and_file = CharField(unique=True, max_length=500)
    start_time = DateTimeField()
    length = DecimalField()
    created_at = DateTimeField(default=datetime.datetime.now)




class PrLog(BaseModel):
    notes = CharField(max_length=1000)
    created_at = DateTimeField(default=datetime.datetime.now)





if not PrVideo.table_exists():
    db.create_tables([PrVideo])

if not PrLog.table_exists():
    db.create_tables([PrLog])