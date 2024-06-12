# find all sundays of specified year
import datetime


def all_sundays(year):
    first_day = datetime.date(year, 1, 1)
    first_dayofweek = first_day.weekday()
    days = datetime.timedelta(6 - first_dayofweek)

    sun = first_day + days

    list_sun = []

    while sun.year == year:
        print(sun)
        list_sun.append(sun)
        sun += datetime.timedelta(7)
    print('There are ' + str(len(list_sun)) + ' sundays in ' + str(year) )

all_sundays(2024)