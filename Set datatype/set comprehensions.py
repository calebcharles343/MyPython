
'''
set() creates an empty set
set accepts only immutable value
'''

s = set()
print(s)
'''
comprehension
'''
s1 = {x for x in range(10)}
print(s1)

s2 = {x**2 for x in [-2,-1,0,1,2]}
print(s2)

s3 = {x for x in (10,5,7,8,12,3) if x%2==0}
print(s3)

s4 = {x.upper() for x in 'philippines'}
print(s4 )
'''
expression
'''

for x in range(1,11):
    s.add(x)
print(s)
