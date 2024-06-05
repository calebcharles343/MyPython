task = 'Checking and removing duplicates in a list'

l1 = [3,5,9,8,3,4,5,9,6,3,7,2]

l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)