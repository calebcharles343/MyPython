punc = ''' !()-_[]{};:'"\,<>./?@#$%^*~ '''
s1 = '[my_python@gmail.com]'
s2 = ''

for x in s1:
    if x not in punc:
        s2 = s2 + x

print(s2)