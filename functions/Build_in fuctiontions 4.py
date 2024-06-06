'''
Built-in Functions

R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()

T
tuple()
type()

V
vars()

Z
zip()

_
__import__()
'''

# class
'''
range()
'''


rep =('=> repr() function in Python returns a string representation '
      'of an object.')
print(rep)
x = 10
print(repr(x))  # Output: '10'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("John", 25)
print(repr(person))  # Output: Person(name='John', age=25)


'''
reversed()function is a built-in function that 
returns an iterator object allowing you to access a 
specified sequence in reverse order.
'''
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)  # Output: [5, 4, 3, 2, 1]

'''

round()

'''

x = 5.76543
rounded_x = round(x, 2)  # Rounds to 2 decimal places
print(rounded_x)  # Output: 5.77


'''
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
'''