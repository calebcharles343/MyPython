import sqlite3

connection = sqlite3.connect('univ.db')

cursor = connection.cursor()

rows = cursor.execute('select name from Students')

# print(rows.fetchone())  # to get first row in the table
# print(rows.fetchmany(3))  # to get specified number of rows in the table
print(rows.fetchall())  # to get all rows in the table


# connection.commit() : only need in DDL & DML query
cursor.close()
connection.close()