from datetime import *

dt1 = datetime(2010, 1, 1, 10, 20, 30)
dt2 = datetime(day=1, month=1, year=2011, hour=10, minute=20, second=30)
tm_delta = dt2 - dt1  # timedelta: difference between two dates
print(tm_delta)
# Division for months
print(divmod(tm_delta.days, 30))  # result: (12months, 5days)
# Division for weeks
print(divmod(tm_delta.days, 7))  # result: (52weeks, 1days)

td1 = timedelta(31)
dt3 = datetime.now()
print(dt3)
print(dt3 + td1)
print(dt3 + tm_delta)