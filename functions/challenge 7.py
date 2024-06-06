# find a pangram sentence
"""
A pangram is a sentence or phrase that uses all 26 l
etters of the alphabet at least once.
"""


def pangram(phrase):
    letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' }
    phr = set(phrase.casefold())
    print(phr)

    if phr >= letters:
        return 'Is a pangram'
    else:
        return 'Is not pangram'


phrase = input('Enter Phrase')

print(pangram(phrase))
