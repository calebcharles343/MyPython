import sqlite3
# creating shop database
'''

connection = sqlite3.connect('shop.db')

cursor = connection.cursor()


# cursor.execute('create table Customer(custid integer primary key, cname text, address text)')
# cursor.execute('create table Product(prodno integer primary key, pname text, price float)')
# cursor.execute('create table Order(orderno integer, custid integer, prodno integer, qty integer, foreign key(custid) references Customer(custid), foreign key(prodno) references foreign key(prodno)')


cursor.execute('create table Orders(orderno int, custid int, prodno int, qty int, foreign key(custid) references Customer(custid), foreign key(prodno) references Product(prodno)')

connection.commit()
cursor.close()
connection.close()
'''

# INSERT INTO TABLE 2 USING INPUTS
connection = sqlite3.connect('shop.db')

cursor = connection.cursor()

'''
# Customer values
custid = int(input('Enter custid '))
cname = input('Enter cname ')
address = input('Enter address ')
'''

'''
# Product values
prodno = int(input('Enter prodno '))
pname = input('Enter pname ')
price = float(input('Enter price '))
'''

# Orders values
orderno = int(input('Enter orderno '))
custid = int(input('Enter custid '))
prodno = int(input('Enter prodno '))
qty = int(input('Enter qty '))

cursor.execute(f'insert into Orders values({orderno}, {custid}, {prodno}, {qty} )')

connection.commit()
cursor.close()
connection.close()
