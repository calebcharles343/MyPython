'''
Built-in Functions

I
id()
input()
int()
isinstance()
issubclass()
iter()
L
len()
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open()
ord()

P
pow()
print()
property()
'''

'''
id() Return the “identity” of an object
'''

'''
input() If the prompt argument is present, it is written to standard 
output without a trailing newline. 
'''

'''
int(string, /, base=10)
Return an integer object constructed from a number or a string, 
or return 0 if no arguments are given.
'''

isints = ('=> isinstance(object, classinfo) Return True if the object '
          'argument is an instance of the classinfo argument, or of a '
          '(direct, indirect, or virtual) subclass thereof. ')
print(isints)

s1 = 'abcde'
n1 = 10
print(isinstance(s1, str))
print(isinstance(n1, int))

'''
issubclass(class, classinfo)
Return True if class is a subclass (direct, indirect, or virtual) of classinfo. 
A class is considered a subclass of itself.
'''

itr = ('=> iter(object, sentinel)'
       'Return an iterator object. The first argument is interpreted very differently) '
       'depending on the presence of the second argument.')

print(itr)
l = [10, 'john', 15.76, 'james']
itere = iter(l)
print(next(itere))
print(next(itere))
print(next(itere))
print(next(itere))

'''
len()
'''

'''
list()
'''

'''
locals()
'''

maap = ('=> map(function, iterable, *iterables)Return an iterator that '
        'applies function to every item of iterable, yielding '
        'the results')
print(maap)


def square(x):
    return x ** 2


numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

'''
max
'''

'''
min
'''

'''
next() used together with iter()
'''

'''
object()
oct() for base conversion
open() to open a file
ord()
'''

poow = ('=? pow() function in Python is a built-in function that allows you '
        'to calculate the power of a number. Here’s how it works:')

result = pow(4, 3)  # Equivalent to 4**3
print(result)

result_mod = pow(4, 3, 5)  # Equivalent to (4**3) % 5
print(result_mod)  # Output: 4


'''
print()
property()
'''