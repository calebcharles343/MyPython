# String Date to Date Object
import datetime

str_date = input('Enter Date in DD-MM-YYYY format: ')

d, m, y = str_date.split('-')  # using unpacking

d1 = datetime.date(int(y), int(m), int(d))
print('Date is: ', d1)