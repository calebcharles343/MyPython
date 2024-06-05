t1 = tuple(x for x in range(10))
print('t1',t1)

t2 = (*(x for x in range(10)),)
print('t2',t2)

t3 = (*(x for x in range(1,10,2)),)
print('t3',t3)

t4 = (*(x for x in 'python'),)
print('t4',t4)

t5 = (*(x for x in 'PyThOn' if x.islower()),)
print('t5',t5)

t6 = tuple(x for x in 'PyThOn' if x.islower())
print('t6',t6)
t7 = tuple(x**2 for x in (1,3,5,7,9))
print('t7',t7)