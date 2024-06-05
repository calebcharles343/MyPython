n = int(input('Enter a number'))
m = n
rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
print('reverse sum is', rev)

if m == rev:
    print('Number is a Palindrome')
else:
    print('Number is Not a Palindrome')