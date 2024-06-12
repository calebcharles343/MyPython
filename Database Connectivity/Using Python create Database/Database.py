import sqlite3

'''
# creating department table
connection = sqlite3.connect('univ.db')

cursor = connection.cursor()

cursor.execute('create table Dept(deptno integer primary key, name text)')

connection.commit()
cursor.close()
connection.close()
'''

'''
# creating student table with foreign key(deptno) references Dept(deptno))

connection = sqlite3.connect('univ.db')

cursor = connection.cursor()

cursor.execute('create table Student(roll integer primary key, name text, city text, deptno integer, foreign key(deptno) references Dept(deptno))')

connection.commit()
cursor.close()
connection.close()
'''

'''
print('Roll  Name     City     Deptno')

for t in allrows:
    print(t[0],'   ',t[1],'  ', t[2], '   ',t[3])
'''

connection = sqlite3.connect('univ.db')

cursor = connection.cursor()

rows = cursor.execute('select roll,name from Students where city not in ("Delhi", "Hyderabad")')

allrows = rows.fetchall()

print(allrows)



cursor.close()
connection.close()
