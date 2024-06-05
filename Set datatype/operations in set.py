a = {1, 2, 3, 5, 7}
b = {5, 7, 9, 10, 11}
x = {1, 2, 3, 5, 7}
y = {5, 7, 9, 10, 11}

op1 = 'union'
c = a.union(b)
print(c)

op2 = 'Intersection'
c = a.intersection(b)
print(c)

op3 = 'Difference'
c = a.difference(b)
print(c)

c = b.difference(a)
print(c)

op4 = 'Symmetric difference'

c = b.symmetric_difference(a)
print(c)


op5 = 'Intersection update'
c = a.intersection_update(b)
print(a)

op6 = 'Difference update'
c = b.difference_update(a)
print(b)

op7= 'Symmetric difference Update'
c = b.symmetric_difference_update(a)
print(b)

'''
issubset()
issuperset()
isdisjoint()
'''


