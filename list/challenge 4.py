task = 'Minimum index sum of two lists'

fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

index1 = 10
index2 = 10

for i in range(len(fav1)):
    index = fav2.index(fav1[i])

    if i + index < index1 + index2:
        index1 = i
        index2 = index
print(fav1[index1], index1 + index2)