"""
steps:
# DDL
1, .open name.bd
2 create table dept(deptno integer primary key not null unique, dname text);
- i.e. dept(deptno datatype constriant not null unique, dname datatype);
3. .tables
4.  create table students(roll integer primary key, name text, city text, deptno integer, foreign key(deptno) references dept(deptno));
- linking dept and student table
6. .tables

#DML
7. insert into dept values(10, 'CSE');
   ...> insert into dept values(20, 'ECE');
   ...> insert into dept values(30, 'Civil');
   ...> insert into dept values(40, 'Mech');

8, insert into dept(dname,deptno) values('Chem', 50);
- to change order
9, select * from dept
-to see tables contents inside dept

#NEXT : inserting value in student table
9, pragma foreign_keys=ON;
- to activate foreign key constraint
10, ;
11, insert into students values(1, 'Charles', 'Abuja', 10);
"""