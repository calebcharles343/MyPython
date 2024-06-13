import os
'''
os.name
os.getlogin()
os.getcwd()
os.chdir()
os.listdir()
os.mkdir()
os.makedirs()
os.remove()
os.rmdir()
os.removedirs()
os.rename()
'''

print(os.name)
print(os.getlogin())
print(os.getcwd())
os.chdir('C:\\Users\\charles\\Desktop\\Mypython') # change working folder
print(os.getcwd())  # get current working folder
print(os.listdir())  # get list of items current working folder

# os.mkdir('C:\\Users\\charles\\Desktop\\Mypython\\child3')  # creates one new folder at the specified directory

# os.makedirs('C:\\Users\\charles\\Desktop\\Mypython\\child4\child5\child6\child7')  # creates nested new folders
# at the specified directory

# os.remove('C:\\Users\\charles\\Desktop\\Mypython\\child4\\child5\\child6\\child7\\text.txt')
# to delete specified file

# os.rmdir('C:\\Users\\charles\\Desktop\\Mypython\\child4')  # to delete specified folder

# os.removedirs('C:\\Users\\charles\\Desktop\\Mypython\\child4')  # to delete specified folders

# os.rename('C:\\Users\\charles\\Desktop\\Mypython\\child4', 'C:\\Users\\charles\\Desktop\\Mypython\\deleteme')
# to rename specified folder

