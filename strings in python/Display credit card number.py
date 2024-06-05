card_no = input('Enter card number')

lastDigits = card_no[15::]
four_star = '*' * 4 + ' '

display = four_star * 3 + lastDigits

print(display)