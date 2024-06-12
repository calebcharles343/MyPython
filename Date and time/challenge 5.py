# Last thursday's date
import datetime


def prev_day(day):
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', ]

    today = datetime.date.today()
    today_dayofweek = today.weekday()
    dayofweek = week_days.index(day)

    diff = dayofweek - today_dayofweek

    if diff < 0:
        new_date = today + datetime.timedelta(diff)
    else:
        new_date = today + datetime.timedelta(-(7 - diff))

    return new_date


print('Today:', datetime.date.today())
print('Previous_day:', prev_day('friday'))
