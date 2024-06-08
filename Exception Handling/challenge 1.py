# Negative age Exception

class NegativeAgeException(Exception):
    pass


def stage(age):
    if age < 0:
        raise NegativeAgeException('Age Should not be Negative')
    elif age >= 0 and age < 13:
        print('kid')
    elif age >= 13 and age < 20:
        print('teen')
    elif age >= 20 and age < 50:
        print('young')
    else:
        print('old')

age = int(input('Enter your age'))

try:
    stage(age)
except NegativeAgeException as e:
    print(e)