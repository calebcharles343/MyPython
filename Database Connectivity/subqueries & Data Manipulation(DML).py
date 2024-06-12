
"""
SUBQUERY
line1 => select city from students where name = 'Ali';
line1 result: Delhi, Mumbai

line2 => select * from students where city in (line1);
line2 result: is all students in line1 result

###############################################
OTHER e.g.
- select * from students where deptno = (select deptno from students where name='Ajay')
- select * from students where deptno > (select deptno from students where name='Chris');
- select * from students where deptno > (select avg(roll) from students);
"""


'''
DML

insert :  
    - insert into dept values(60, 'EEE')

delete
    - delete from dept where dname = 'EEE';
update
    - update dept set dname = 'Aero' where deptno = 50;

'''