print('before try')
try:
    a = int(input('Enter numerator'))
    b= int(input('Enter denominator'))
    c = a // b
except ZeroDivisionError as err:
    print(err)
else:
    print('Division is', c)
finally:
    print('Finally block')
print('outside try-except-else')
