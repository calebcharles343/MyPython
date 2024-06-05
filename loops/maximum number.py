num_of_nos = int(input('Enter number of numbers'))

max = int(input('Enter a num'))
count = 0
while count < num_of_nos:
    n = int(input('Enter a number'))
    if n > max:
        max = n
    count = count + 1
print('max no is', max)