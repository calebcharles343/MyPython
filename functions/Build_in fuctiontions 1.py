'''
Built-in Functions

A
abs()
aiter()
all()
anext()
any()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
callable()
chr()
classmethod()
compile()
complex()
'''

ab = ('=> abs() Returns the absolute value of a number. It works for integers, '
      'floating-point numbers, and objects implementing')
print(ab)
a = -15
print(abs(a))

asc = '=> ascii() return a string containing a printable representation of an object'
print(asc)
print(ascii('A'))
print(ascii(10))
print(ascii('\u0521'))

binary = '=> bin() Converts an integer to a binary string prefixed with “0b”'
print(binary)
print(bin(10))

bol = '=> bool() Converts x to a Boolean value (True or False) using standard truth testing.'
print(bol)
print(bool(1))
print(bool(0))

bytary = '=> bytearray() Return a new array of bytes and its mutable'
print(bytary)
print(bytearray(10))

byt = '=> bytes() Return a new array of bytes and its not mutable'
print(bytary)
print(bytes(10))

clb = '=> callable() Return True if the object argument appears callable, False if not.'
print(clb)
print(callable(bool))
print(callable(10))

character = '=> chr() Return the string representing a character whose Unicode code point is the integer i. '
print(character)
print(chr(65))

od = '=> ord() does then opposite of chr()'
print(od)
print(ord('A'))

cpl = '=> complex() creates complex datatype'
print(cpl)
print(complex(10))

dct = '=> Creates a new dictionary (a collection of key-value pairs)'
print(dct)
print(dict())

directory = '=> dir() details of a particular data class'
print(directory)
print(dir(int))
print(dir(str))

division_Mod = ('=> divmod() Return an enumerate object. '
                'iterable must be a sequence, an iterator, '
                'or some other object which supports iteration')
print(division_Mod)
print(divmod(11,3))
print(divmod(45,23))