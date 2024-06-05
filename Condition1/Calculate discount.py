amount = int(input('Enter Amount'))

if amount <= 1000:
    discount = amount * 10 / 100
elif 1000 < amount <= 5000:
    discount = amount * 20 / 100
elif 5000 < amount <= 10000:
    discount = amount * 30 / 100
elif 10000 < amount:
    discount = amount * 50 /100
discAmount = amount - discount

print('pay', discAmount)
