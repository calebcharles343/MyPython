'''
dict() creates empty dictionary
'''

dict1 = dict()
dict1['apple'] = 'red'
dict1['mango'] = 'yellow'

print(dict1)

'''
loop insert
'''
for x in range(1,6):
    dict1[x] = x**2
print(dict1)

'''
{} also creates a dictionary
'''
dict5 = {}
print(type(dict5))
for x in range(1,6):
    dict5[x] = 2*x
print(dict5)


'''
iterable pairs
'''
dict2 = dict(((1,2), (2,4), (3,6)))
print(dict2)

dict2 = dict(('ab', 'cd', 'ef'))
print(dict2)

l1 = ['a','b','c']
l2 = ['apple', 'ball', 'cat']

dict3 = dict(zip(l1,l2))
print(dict3)

'''
enumerate
'''
for item in enumerate(l1):
    print(item)

dict4 = dict(enumerate(l1))
print(dict4)

'''
expression
'''
dict6 = {x:x**2 for x in range(1,5)}
print(dict6)

dict7 = dict((x,x**2) for x in range(1,5))
print(dict7)

dict8 = dict((x,y) for x,y in zip(l1,l2))
print(dict8)

for x,y in enumerate(l1):
    print(x,y)
dict9 = {x+1:y for x,y in enumerate(l2)}
print(dict9)