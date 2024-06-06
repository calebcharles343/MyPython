'''
Built-in Functions
E
enumerate()
eval()
exec()

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()
'''

enume = ('=> enumerate() Return an enumerate object. iterable must '
         'be a sequence, an iterator, or some other object '
         'which supports iteration.')
print(enume)
l = ['A','B','C','D','E']
e = enumerate(l)
for i in e:
    print(i)

eva = '=> eval() return the result of the evaluated expression.'
print(eva)
print(eval('3*10+15/3'))
print(eval('2**4+9'))

exe = ('=> exec() This function supports dynamic execution of '
       'Python code. object must be either a string or a code object..')
print(exe)
s='x=10\ny=20\nprint(x+y)'
print(exec(s))

flt = ('=> filter() Construct an iterator from those elements of '
       'iterable for which function is true')
print(flt)
l= [3,6,7,9,12,14,19,21]
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

f = filter(even, l)
print(f)
for i in f:
    print(i)
f = filter(lambda x: x> 10, l)
print(f)
for i in f:
    print(i)

flt = '=> float() converts numbers to float data type'
print(flt)
print(float(-10))

fmt = ('=> format(value, format_spec) Convert a value to a “formatted” '
       'representation, as controlled by format_spec.')
print(fmt)
f = 12.54634
print(format(f,'E'))

fznset = ('=>frozenset() Return a new frozenset (immutable)object, optionally with '
          'elements taken from iterable')
print(fznset)
print(frozenset({1,2,3}))

'''
getattr() Return the value of the named attribute of object. 
name must be a string

'''

glb = ('=> Return the dictionary implementing the current module '
       'namespace. For code within functions, this is set when '
       'the function is defined and remains the same regardless '
       'of where the function is called.')
print(glb)
print(globals())

hasat = ('=> hasattr(object, name) The arguments are an object and a '
         'string. The result is True if the string is the name of one '
         'of the object’s attributes, False if not.')
print(hasat)

s1 = 'abcde'
print(hasattr(s1, 'lower'))
print(hasattr(s1, 'isdigit'))

hsh = ('=> hash(object) Return the hash value of the object '
       '(if it has one). Hash values are integers. ')
print(hsh)
print(hash(s1))

'''
help() Invoke the built-in help system.
'''
'''
hex()
'''