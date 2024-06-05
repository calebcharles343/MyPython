task = 'find the number of occurrences of each item'
l1  = ['A', 'B', 'C', 'D', 'E','A', 'B','E','N','D','B','E']

result = []

for x in l1:
    if x not in result:
        result.append(x)
        count = l1.count(x)
        result.append(count)
print(result)