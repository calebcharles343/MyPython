num = int(input('Enter number'))
n = num

bin = ''


while num > 0:
    r = num % 2
    num = num // 2
    bin =str(r) + bin



print('bin of', n, 'is', bin)