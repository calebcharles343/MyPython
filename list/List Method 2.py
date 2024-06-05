list1 = [5,6,7,8,9]

'''
pop(x) this deletes an element in an array
this modifies the same list 
del VERSION IS = del list1[0]
'''
list1.pop(0)
print(list1)

'''
remove(x) this removes the element mentioned
this modifies the same list 
'''
list1.remove(7)
print(list1)

'''
clear() this deletes every element in a list
'''
list1.clear()
print(list1)


list2 = [5,6,7,8,9,5]
'''
index(x[,start[,end]]) this finds element in a list
'''
print(list2.index(5))

'''
count(x) this counts the occurrence of mentioned element in a list
'''
print(list2.count(5))

'''
reverse() this reverses a list form end to start
'''
list3 = [5,6,7,8,9,5,14]
x = list3.reverse()
print(x)

'''
sort(x,key = None, reverse = false)
this modifies the same array while sorted() creates a new array
'''
y = list3.sort(key=str.lower(), reverse = True)
print(y)


