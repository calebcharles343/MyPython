list = [10,20,['a','b',['c', 'd']],30,40]

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[9,8,7],[6,5,4],[3,2,1]]
c = []

for i in range(len(a)):
    s = []
    for j in range(len(a[0])):
        s.append(a[i][j] + b[i][j])
    c.append(s)
print(c)