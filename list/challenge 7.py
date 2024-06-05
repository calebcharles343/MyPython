challenge = 'string to morse code'
codes = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '... .', '. .', '.___']

test = 'deface'
morse_str = ''

for x in test:
    morse_str += codes[ord(x)- 97] + "  "
print(morse_str)