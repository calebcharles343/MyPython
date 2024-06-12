import datetime

dt1 = datetime.datetime(2010, 1, 1, 10, 10, 10)
dt2 = datetime.datetime(day=1, month=1, year=2011, hour=10, minute=10, second=10)
print(dt2 - dt1)
print(dt2 > dt1)
print(dt2 < dt1)

# Combine
dat1 = datetime.date(2015, 1, 1)
tim1 = datetime.time(10, 10, 10)

dt3 = datetime.datetime.combine(dat1, tim1)
print(dt3)

# Note can compare but cannot subtract datetime.time() from datetime.time()
