dict1 = {101: 'john', 102: 'smith', 103: 'mark', 104:'david'}

'''
NOTE
differences of dict1[101] and dict1.get(101): if element is not present in dictionary 
dict1[101] gives an error
    while 
dict1.get(101) ignores error
'''

for i in dict1:
    print(i, dict1[i])

print('###############')

for i in dict1:
    print(i, dict1.get(i))

'''
keys(), values() and items()
'''

print('keys() =>',dict1.keys())

print('values() =>',dict1.values())

print('items() =>',dict1.items())

'''
loop
'''
for k in dict1.keys():
    print(k,dict1[k])

for xy in dict1.items():
    print(x,y)
