import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime("%d/%m/%y %H:%M:%S:%f"))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime("%d/%m/%y"))

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime("%H:%M:%S:%f"))

print(now)
# d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=365)
# d = datetime.timedelta(hours=1)
# d = datetime.timedelta(minutes=10)
# d = datetime.timedelta(seconds=50)
# d = datetime.timedelta(milliseconds=1000)
print(now - d)

import time

print("###")
time.sleep(1)
print("###")
print(time.time())

import os
import shutil

file_name = "section8/test.txt"
if os.path.exists(file_name):
    shutil.copy(file_name, "{}{}.bak".format(file_name, now.strftime("%Y%m%d_%H%M%S")))
