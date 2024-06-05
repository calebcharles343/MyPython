emailId = input('Enter email address')

atrate = emailId.find('@')

print(atrate)

print('user ID:', emailId[:atrate])
print('domain name:', emailId[atrate+1:])