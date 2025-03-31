

from calendar import month
import calendar
from datetime import *
from datetime import datetime
import time

import pytz

now = datetime.now()
print("Now---------",now)

'''
2020-03-30 10:20:51
2020-03-30 10:20
2020-03-30 10
2020-03-30
30-03-2020
03-30-2020
30-Mar-2020
30-Mar-20
'''
#now = datetime.strptime(now,"YYYY-MM-DD")
#print("Now---------",now)
#now = now.astimezone(pytz)
#print("Now---------",now)
# EPOCH Time
epoch = time.time()
print("Epoch        Time :", epoch)

# Current Time
current_time = time.ctime()
print("Current time      :", current_time)


# Current Date Time
now = datetime.now()
print("Current Date time :",now)
print("Date now          : {}-{}-{}".format(now.day, now.month, now.year))

# Today's date and Time

tdm = datetime.today()
print("Today's Date & Time :", tdm)
td = date.today()
print("Today's Date        :", td)
print("Today's Date        :", td.strftime("%d, %B, %Y"))


# CALENDAR
yy = int(input("Enter year : "))
mm = int(input("Enter month: "))

str1 = month(yy, mm)
print("Calendar for Current Month", str1)

year = int(input("Enter year :"))
print(calendar.calendar(year, 2, 1, 8, 3))

