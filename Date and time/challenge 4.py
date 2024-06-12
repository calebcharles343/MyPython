# calculate age:

from datetime import date


def age(date_of_birth):
    today = date.today()
    years = today.year - date_of_birth.year

    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        years -= 1
    return years


print('Age is',age(date(1992, 9, 28)))
