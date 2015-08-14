from db import *
import shortcuts

data = Monitor.select().where(Monitor.id == 1).first()



s = str(data)

print(s)