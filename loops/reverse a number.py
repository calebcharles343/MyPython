n = int(input('Enter a number'))
rs = 0
while n > 0:
    r = n % 10
    n = n // 10
    rs = rs * 10 + r
print('reverse sum is', rs)