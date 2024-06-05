list1 = [5,6,7,8,9]
'''
Iterating a list means visiting all the members of a list or collection
'''

'''
for loop
'''
print('for loop')
for i in range(len(list1)):
    print(list1[i])

'''
range loop
'''
print('range loop')
for i in range(2,len(list1)):
    print(list1[i])

'''
reverse range loop
'''
print('reverse range loop')
for i in range(len(list1)-1,-1,-1):
    print(list1[i])

'''
While loop
'''
print('While loop')

i = 0
while i < len(list1):
    print(list1[i])
    i += 1