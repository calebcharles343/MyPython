from collections import Counter
l = ['Mark', 'John', 'David', 'Mark', 'Jonny', 'Jonny', 'Mark', 'James', 'Mathew']

counter = Counter(l)

print(counter)

print(counter.get('Mark'))
print(counter.keys())
print(counter.values())

counter.update({'Charles':4})  # to add

print(counter)

print(counter.elements())

for i in counter.elements():
    print(i)

counter.pop('James')  # to delete

print(counter)

counter.popitem()  # to delete recent item

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))

'''
clear()
copy()
'''

