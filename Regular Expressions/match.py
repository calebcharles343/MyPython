from re import*
print(match('a', 'a').group())
print(match('b', 'b').group())
print(match('ajb', 'ajb').group())

'''
[a-z] this represents a single letter 
'''
'''
[a-z]+ this represents a range from letter a to z 
'''
'''
[a-zA-Z0-9]+ this represents a range from letter a to z, A to Z, 0 to 9
'''

'''
check for
re.compile()
re.search()
re.match()
re.findall()
re.sub()
'''