'''
Aggregate Functions
    -select count(*) from students;
    -select count(roll) from students;
    -select count(name) from students;
    -select count(distinct name) from students;
    -select max(roll) from students;
    -select min(roll) from students;
    -select sum(roll) from students;
    -select avg(roll) from students;
-select max(roll),city from students group by city;
-select count(roll),city from students group by city;
-select sum(roll),city from students group by city;
Set Operations: union intersection and except(difference)
    - select * from students where city = 'Delhi' union select * from students where city = 'Kolkata';
    - select name from students where city = 'Delhi' union select name from students where city = 'Mumbai';(no copies)
    -  select name from students where city = 'Delhi' intersect select name from students where city = 'Mumbai';
    (what's common)
    -  select name from students where city = 'Delhi' except select name from students where city = 'Mumbai';
    (what's common)
Subquery
DML
'''