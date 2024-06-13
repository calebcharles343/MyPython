import os
import time
'''
CSv: means comma separated values

os.path.exits()
os.path.isfile()
os.path.isdir()
os.path.split()
os.path.join()
os.path.basename()
os.path.dirname()
os.path.getmtime()
os.path.getatime()
os.path.relpath()
os.path.abspath()
'''

print(os.path.exists('C:\\Users\\charles\\Desktop\\Mypython\\univ.db'))
print(os.path.isfile('C:\\Users\\charles\\Desktop\\Mypython\\univ.db'))
print(os.path.isdir('C:\\Users\\charles\\Desktop\\Mypython'))
print(os.path.split('C:\\Users\\charles\\Desktop\\Mypython\\univ.db'))
print(os.path.join('C:\\Users\\charles\\Desktop\\Mypython', 'univ.db'))
print(os.path.basename('C:\\Users\\charles\\Desktop\\Mypython\\univ.db'))
print(os.path.dirname('C:\\Users\\charles\\Desktop\\Mypython\\univ.db'))
print(time.ctime(os.path.getmtime('C:\\Users\\charles\\Desktop\\Mypython\\univ.db')))
print(time.ctime(os.path.getatime('C:\\Users\\charles\\Desktop\\Mypython\\univ.db')))
print(time.ctime(os.path.getctime('C:\\Users\\charles\\Desktop\\Mypython\\univ.db')))

os.chdir('C:\\Users\\charles\\Desktop\\Mypython\\child1')
print(os.getcwd())
print(os.path.relpath('C:\\Mypython\\child2\\child2.txt'))
print(os.path.abspath('..\\..\\..\\..\\..\\Mypython\\child2\\child2.txt'))
