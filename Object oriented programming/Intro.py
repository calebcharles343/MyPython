# Object-Oriented Programming (OOP),
# NOTE:  abstraction simplifies, while encapsulation protects.
# Both are essential for building robust and maintainable software!

'''
Object-Oriented Programming: THis is a fundamental
paradigm in Python that empowers developers to build modular,
maintainable, and scalable applications.

1. Class:
   - A class is a blueprint or prototype for creating objects.
   - It defines attributes (variables) and methods (functions)
   that the objects will have.
   - Example:
     ```python
     class Dog:
         def __init__(self, breed, age):
             self.breed = breed
             self.age = age

     my_dog = Dog("Golden Retriever", 3)
     ```

2. Object:
   - An object: is an instance of a class.
   - It has state (attributes) and behavior (methods) associated
   with it.
   - Example:
     ```python
     print(my_dog.breed)  # Output: Golden Retriever
     ```

3. Inheritance:
   - Inheritance allows a class (subclass) to inherit attributes
   and methods from another class (superclass).
   - It promotes code reuse and hierarchy.
   - Example:
     ```python
     class Labrador(Dog):
         def __init__(self, breed, age, color):
             super().__init__(breed, age)
             self.color = color

     my_labrador = Labrador("Labrador Retriever", 2, "Yellow")
     ```

4. Polymorphism:
   - Polymorphism enables objects of different classes to be
   treated uniformly.
   - It allows method overriding and dynamic behavior.
   - Example:
     ```python
     def describe_pet(pet):
         print(f"{pet.breed} is {pet.age} years old.")

     describe_pet(my_dog)       # Output: Golden Retriever is 3 years old.
     describe_pet(my_labrador)  # Output: Labrador Retriever is 2 years old.
     ```

5. Encapsulation:
   - Encapsulation hides implementation details and exposes a simple interface.
   - It protects data by restricting direct access.
   - Example:
     ```python
     class BankAccount:
         def __init__(self, balance):
             self._balance = balance  # Protected attribute

         def get_balance(self):
             return self._balance

     my_account = BankAccount(1000)
     print(my_account.get_balance())  # Output: 1000
     ```

6. Abstraction:
   - **Abstraction** focuses on essential features while hiding implementation details.
   - It simplifies complex systems.
   - Example:
     ```python
     from abc import ABC, abstractmethod

     class Shape(ABC):
         @abstractmethod
         def area(self):
             pass

     class Circle(Shape):
         def __init__(self, radius):
             self.radius = radius

         def area(self):
             return 3.14 * self.radius ** 2
     ```

Remember, OOP enhances code organization, reusability, and maintainability! 🚀 If you'd like more examples or details, feel free to explore [additional resources](https://www.geeksforgeeks.org/python-oops-concepts/). 😊

Source: Conversation with Copilot, 6/9/2024
(1) Python OOPs Concepts - GeeksforGeeks. https://www.geeksforgeeks.org/python-oops-concepts/.
(2) Object Oriented Programming Python | Python OOP Concepts | Edureka. https://www.edureka.co/blog/object-oriented-programming-python/.
(3) Object-Oriented Programming in Python - freeCodeCamp.org. https://www.freecodecamp.org/news/object-oriented-programming-in-python/.
(4) Basic OOPs Concepts in Python | Object Oriented Programming. https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/.
(5) Object-Oriented Programming (OOP) in Python 3 – Real Python. https://realpython.com/python3-object-oriented-programming/.
'''
"""
Encapsulation:
in Python refers to the practice of hiding the implementation details of an
object or class, and only exposing a public interface for interacting with
it. Let’s dive into the details:

What Is Encapsulation?
Encapsulation is one of the fundamental concepts in object-oriented
programming (OOP).

It describes the idea of wrapping data and methods within one unit.
By doing so, it restricts direct access to variables and methods,
preventing accidental modification of data.
"""

'''
Abstraction: simplifies complex reality by modeling classes based on the 
essential properties and behaviors an object should possess. 
Let’s explore this concept further:

What is Abstraction?
Abstraction focuses on hiding the internal implementations of a process 
or method from the user.

Users interact with an object based on its essential features, 
without needing to understand the underlying complexity.

For example, when you drive a car, you don’t need to know how every 
individual part works; you simply use the car as a whole.
'''

'''
inheritance 
is a fundamental concept in Object-Oriented Programming (OOP). 

Superclass (Parent Class):
The existing class from which a child class inherits is called 
the superclass or parent class.

The superclass provides a blueprint for creating new classes.

Example: Suppose we have a Person class with properties like 
firstname and lastname.

Subclass (Child Class):
The new class created by inheriting from the superclass is called 
the subclass or child class.

The subclass inherits all the methods and properties from the parent class.

Example: Let’s create a Student class that inherits from the Person class.

'''

'''
Polymorphism 
is a core concept in Object-Oriented Programming (OOP). 

What is Polymorphism?
Polymorphism refers to the ability of a single interface 
(such as a method or function) to support entities of multiple types.

It allows different objects to respond uniquely to the same method call.
In Python, polymorphism is inherent in its de
'''


