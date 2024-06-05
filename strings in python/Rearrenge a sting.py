s1 = 'AbcDEfgHi'

lower = ''
upper = ''

for x in s1:
    if x.islower():
        lower += x
    else:
        upper += x
s2 = lower + upper
print(s2)