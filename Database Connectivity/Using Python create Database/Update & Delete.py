import sqlite3

connection = sqlite3.connect('univ.db')

cursor = connection.cursor()


# cursor.execute('update Dept set dname = "Chem" where dname="Mech"')
# cursor.execute('update Students set city = "Bhopal" where roll=15')
# cursor.execute('delete from Students where roll=15')
cursor.execute('delete from Dept where deptno = 40')

connection.commit()
cursor.close()
connection.close()
