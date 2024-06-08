'''

file = open('Prop.txt', 'r')
file.close()
print(file.name)
print(file.mode)
print(file.closed)
'''

'''

file = open('Prop.txt', 'r')

line = file.readline() # Reads line by line
print(line, end =  '')

line = file.readline()
print(line)

'''
'''
file = open('Prop.txt', 'r')

lines = file.readlines() # Returns a list of lines
print(lines , type(lines))

for line in lines:
    print(line, end= '')
    
'''

file = open('copying binary files/Prop.txt', 'w')
# str1 = 'python is simple\nit is easy\n everything is an object'
# file.write(str) # writes in the str provided

list1 = ['python is simple\n', 'it is easy\n', 'everything is an object\n']
file.writelines(list1)  # writes a list line by line

'''
file.flush() : ensure all items sent from the buffer to file 
'''