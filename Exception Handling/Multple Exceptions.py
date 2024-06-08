l = [10,20,30,40,50]

try:
    index = int(input('Enter index'))
    print(l[index])
except IndexError as msg:
    print('invalid index', msg)
except ValueError as msg:
    print('Enter only integer value', msg)

print('Terminate gracefully')


l2 = [10,20,30,40,50]

try:
    index = int(input('Enter index'))
    print(l2[index])
except (IndexError, ValueError) as msg:
    print(msg)

print('Terminate gracefully')