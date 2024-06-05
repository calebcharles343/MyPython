list1 = [5,6,7,8,9]

'''
append(x) this increases an array by 1
modifies the same list
SLICE VERSION IS = list1[5:5] = [10] 
'''
list1.append(10)
print(list1)

'''
extend(iterable) this extends an array by more than 1 
this modifies the same list 
SLICE VERSION IS = list1[len(list1):] = [10,11,12]
'''
list1.extend([10,11,12])
print(list1)

'''
insert(i,x) this insert an element at a specific index position 
this modifies the same list also
'''
list1.insert(0,10)
print(list1)

'''
copy() this returns a shallow copy of the original list
this creates a new array
'''
list2 = list1.copy()
print(list2)


