"""
import datetime

today = datetime.date.today()
now = datetime.datetime.now()

print(today)
print(now)


print(f"year is:{now.year}")
print(f"month is: {now.month}")
print(f"day is:{now.day}")
print(f"hour is:{now.hour}")
print(f" minutes is:{now.minute}")
print(f" seconds is:{now.second}")


formatting date and time
--------------------------
-->strftime() is used to firnate date and time


import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))


import datetime
date_1=datetime.date(2025,6,1)
date_2=datetime.date(2026,6,1)
differ=date_2-date_1
print(differ)

timedelta
---------------
import datetime

today = datetime.date.today()
future = today - datetime.timedelta(days=7)

print(future)


import datetime
day=datetime.date.today()
print(day.weekday())
print(day.ctime())

import calendar
import datetime
today=datetime.date.today()
year=today.year
month=today.month
print(calendar.month(year, month))

year=2027
print(calendar.calendar(2028))
"""
from datetime import datetime, timedelta
import time

send_time = datetime.now() + timedelta(hours=1)

while datetime.now() < send_time:
    time.sleep(60)  # check every minute

print("Send email now!")




