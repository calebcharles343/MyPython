'''
file = open('modeDemo.txt', 'w')
file.write('Hello!\n')
file.write('How are you\n')
file.write('Do yo know python\n')

file.close()
'''

'''
file = open('modeDemo.txt', 'a')
file.write('I am leaning python!\n')
file.write('it is a very easy language\n')
file.write('i am practising everything\n')

file.close()

'''


file = open('copying binary files/modeDemo.txt', 'r+')
str1 = file.read(10)
print(str1)

file.write('Good by!\n')
file.close()