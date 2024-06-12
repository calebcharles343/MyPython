import sqlite3

# Shop Queriese

connection = sqlite3.connect('shop.db')

cursor = connection.cursor()

rows = cursor.execute('select * from Orders')

# print(rows.fetchone())  # to get first row in the table
# print(rows.fetchmany(3))  # to get specified number of rows in the table
print(rows.fetchall())  # to get all rows in the table


# connection.commit() : only need in DDL & DML query
cursor.close()
connection.close()