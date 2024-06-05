l1 = [x for x in range(10)]
print(l1)

l2 = [x**2 for x in range(1,6)]
print(l2)

l3 = [x for x in(10,5,7,8,12,3) if x % 2 == 0]
print(l3)

l4 = [x.lower() for x in 'Python']
print(l4)

l5 = [x for x in 'abc12de-$fg4$hi2' if x.isalpha()]
print(l5)

'''
data = input('enter names')
l6 = data.split()
print(l6)

'''
l6 = input('enter names').split()
print(l6)