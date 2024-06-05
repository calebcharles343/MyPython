task = 'Concatenate all integer from a list to a single number'

l1 = [str(x) for x in[ 3,5,10,7,12]]

s1 = ''

for x in l1:
    s1 += x
print(int(s1))