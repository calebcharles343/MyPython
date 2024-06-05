password1 = input('Enter password')
password2 = input('Confirm password')

if password2 == password1:
    print('Password match')
else:
    if password1.casefold() == password2.casefold():
        print('please check letter cases')
    else:
        print('Password not matching try again')
