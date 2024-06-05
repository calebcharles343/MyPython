a = int(input('Enter initial term'))
d = int(input('Enter common Difference'))
n = int(input('Enter number of terms'))

for t in range(a, a + n * d, d):
    print(t) 