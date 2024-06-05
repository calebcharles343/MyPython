dict1 = {'abacus': 'a calculator', 'bachelor': 'unmarried person', 'cable': 'strong rope'}

print(dict1)
'''
read a keys value
'''
print(dict1['abacus'])

dict2 = {101: 'john', 102: 'smith', 103: 'mark', 104:'david'}
print(dict2)
print(dict2[101])

'''
change value of key
'''
dict2[101] = 'mathew'
print(dict2[101])

'''
insert new key and value 
'''
dict2[105] = 'charles'
print(dict2)

'''
delete key and value
'''
del dict2[104]
print(dict2)

'''
dictionary loop
'''

for i in dict2:
    print(i, dict2[i])