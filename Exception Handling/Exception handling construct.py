l = [10,20,30,40,50]

try:
    index = int(input('Enter index'))
    print(l[index])
except:
    print('invalid index')

print('Terminate gracefully')