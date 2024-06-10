# Static method
class Calculator:
    pass

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


cal = Calculator()
print(cal.add(10, 5))
print(cal.sub(10, 5))
print(cal.mul(10, 5))
print(cal.div(10, 5))
