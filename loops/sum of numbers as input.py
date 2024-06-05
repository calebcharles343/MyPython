num_of_nos = int(input('Enter number of numbers'))

sum = 0
count = 0
while count < num_of_nos:
    n = int(input('Enter a number'))
    sum = sum + n
    count = count + 1
print('sum is', sum)