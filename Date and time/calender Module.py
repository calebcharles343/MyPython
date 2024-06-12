from calendar import *

print(firstweekday())
print(isleap(2024))
print(leapdays(2000, 2022))  # is a leap year
print(weekday(2000, 1, 1))  # weekday
print(weekday(2022, 3, 16))  # weekday

print(prmonth(2022, 3))  # month
print(prmonth(2022, 4, 5, 2))  # month with width and line gap

# Iteration
c = Calendar()
print(c)
for i in c.iterweekdays():
    print(i)

for i in c.itermonthdays(2022, 3):
    print(i)

for i in c.itermonthdates(2022, 3):
    print(i)

print(c.monthdatescalendar(2022, 3))

# Text calender
text_calender = TextCalendar()
print(text_calender.prmonth(2022, 3))
print(text_calender.pryear(2022, 3))

print(text_calender.formatmonth(2022,3).split('\n'))

for i in text_calender.formatmonth(2022,3).split('\n'):
    print(i)

# HTML calender
html_calender = HTMLCalendar()  # browser
print(html_calender.formatmonth(2023, 3))


