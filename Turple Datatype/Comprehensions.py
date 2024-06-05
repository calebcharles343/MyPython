tuple1 =  ('jack', 45, 38.6, False, 5+6j, 'Jill', 45)
print(type(tuple1))

'''
packing
'''
t1 = 10,20,30,40,50
print(t1)

'''
unpacking
'''
a, b, c, d, e = t1

print(a,b,c,d,e)

'''
rest packing
'''

a, b, *c = t1

print(a, b, c,)