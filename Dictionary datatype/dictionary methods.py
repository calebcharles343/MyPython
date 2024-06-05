dict1 = {101: 'john', 102: 'smith', 103: 'mark', 104:'david'}
'''
copy()
'''
dict2 = dict1.copy()
print(dict2)

dict2[101] = 'charles'

print(dict1)
print(dict2)

print('Id of', dict1[101], id(dict1[101]))
print('Id of', dict2[101],id(dict2[101]))

print('Id of', dict1[102],id(dict1[102]))
print('Id of', dict2[102],id(dict2[102]))

'''
update()
'''
dict3 = {101:'production', 102: 'accounts', 103: 'sales', 104: 'inventory'}
dict4 = {105: 'designing', 106: 'package'}

dict3.update(dict4)
print(dict3)
'''
setdefault() insert key and value if its not there
'''
print(dict3.setdefault(102))
print(dict3.setdefault(110, 'ads'))
print(dict3)

'''
fromkeys()
'''
l1 = [11,22,33,44]
dict5 = {}

print(dict5.fromkeys(l1,100))

'''
pop(key), default(), popitem() = 'removes last item', clear()
'''
dict1 = {101: 'john', 102: 'smith', 103: 'mark', 104:'david'}
dict1.pop(104)
print(dict1)

dict1.popitem()
print(dict1)

dict1.clear()
print(dict1)
