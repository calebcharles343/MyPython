s1 = {10,20,30,40,50}
'''
add() single value
'''
s1.add(60)
s1.add('james')
print(s1)
'''
copy()
'''
s2 = s1.copy()
print(s2)

'''
update() adds multiple values
'''
s1.update((50,60,70))
s1.update([11,22,33])
s1.update('python')
print(s1)
'''
pop() deletes a single element
'''
s1.pop()
print(s1)

'''
discard() deletes an element mentioned and ignores error if the 
mentioned element is not present in the set
'''
s1.discard('p')
print(s1)
'''
remove() deletes an element mentioned and gives error if the 
mentioned element is not present in the set
'''
s1.remove(30)
print(s1)
'''
clear() deletes all elements 
'''
s1.clear()
print(s1)
