# write function with positional arguments only

def message(name, profession, /):
    print('My name is', name + ',', 'I am a', profession)


message('Charles', 'developer')
