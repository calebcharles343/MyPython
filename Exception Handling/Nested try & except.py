try:
    a = int(input('Enter first number'))
    try:
        b= int(input('Enter second number'))
        try:
            c = a // b
            print(c)
        except ZeroDivisionError as e:
            print(e)
    except ValueError:
        print('Value Error inner')
except ValueError:
    print('Value Error outer')
