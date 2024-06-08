# file_handler = open(filename, mode)
file = open('my data.txt', 'r')
str1 = file.read(6)
print(str1)
str2 = file.read(10)
print(str2)

file.close() 