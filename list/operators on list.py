lis1 = [1,2,3,4,5,6,7,8,9,10]
'''
List operators
index op = [] 'to read or mutate'
slice op = [:] '[start:end:step], creates a new list or mutates'
concat op = + 'adds two separate list together'
multiply op = * 'multiplies a list'
condition op = in 'e.g for x in'
condition op  = not in 'e.g for x not in'
'''

'''
Using slice to mutate a list
'''
lis1[0:3] = [10,20,30]
print(lis1)
lis1[0:3] = [10,20,30,40,50,60]
print(lis1)

lis1.extend([11,12])
print(lis1)