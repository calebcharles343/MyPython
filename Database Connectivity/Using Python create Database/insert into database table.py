import sqlite3
'''
# INSERT INTO TABLE 1
connection = sqlite3.connect('univ.db')

cursor = connection.cursor()

#cursor.execute('insert into Dept values(10,"CSE")')
cursor.execute('insert into Dept(name, deptno) values("ECE", 20)')

connection.commit()
cursor.close()
connection.close()
'''

# INSERT INTO TABLE 2 USING INPUTS
connection = sqlite3.connect('univ.db')

cursor = connection.cursor()

dno = int(input('Enter Deptno'))
dname = input('Enter dname')


#cursor.execute('insert into Dept values(10,"CSE")')
cursor.execute(f'insert into Dept values({dno}, "{dname}")')

connection.commit()
cursor.close()
connection.close()
