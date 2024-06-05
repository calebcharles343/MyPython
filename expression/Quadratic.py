import math

a = int(input('Enter value a'))
b = int(input('Enter value b'))
c = int(input('Enter value c'))

root1 =(-b + math.sqrt(b**2 - 4 * a * c) )/ (2 * a)
root2 =(-b - math.sqrt(b**2 - 4 * a * c) )/ (2 * a)

print('Roots are', root1, root2)

# Square root cannot find out the result for a negative value
# Always check if expression b**2 - 4 * a * c is greater than 0
