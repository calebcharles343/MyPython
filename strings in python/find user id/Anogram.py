s1 = input('Enter a 1st string')
s2 = input('Enter a 2nd string')

if len(s1) != len(s2):
    print('Not an Anogram')
else:
    for x in s1:
        if x not in s2:
            print('Not an Anogram')
            break
    else:
        print('Anogram')
'''
isAnogram = sorted(s1) == sorted(s2)

print(isAnogram)
'''


