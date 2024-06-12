from datetime import *

dt1 = datetime(2010, 1, 1, 10, 20, 30)
print(dt1)

print('####### Format: from time to string #######')
print(dt1.strftime('%d %B, %A %Y, %H:%M:%S'))  # In full spelling
print(dt1.strftime('%d %b, %a %Y, %H:%M:%S'))  # In short spelling
# print(dt1.strftime('%-d %B, %A %Y, %H:%M:%S'))

print('####### Format: from string to python object #######')

str1 = '10 jan 2015, 10:15:30'
print(datetime.strptime(str1, '%d %b %Y, %H:%M:%S'))
