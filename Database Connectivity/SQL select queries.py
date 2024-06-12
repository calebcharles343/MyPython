# SQL QUERY LANGUAGE
'''
#Clauses

select - specifying columns of a relation needed to retrieve data
- filtering column e.g. remove or keep row that matches a condition

from - specifying name of data source needed to retrieve data
-(select and from E.G.) select name from students; OR select roll, name, city from students: (to get everything)
- select * from students; (to get all rows about student )
- select deptno from students (to get all student deptno);
- select distinct deptno from students; (to get all student unique deptno);

join - fetching data from multiple sources
    - select * from students join dept on students.deptno=dept.deptno;
    - select * from students S join dept D on S.deptno=D.deptno;(to rename and join)

NOTE:  select * from students,dept; will multiply every single student by all dept rows
    -  select * from students,dept where students.deptno=dept.deptno;(to get student and with their department number)

where - used for specifying condition upon one or more rows.
- filtering row e.g. remove or keep row that matches a condition
- select * from students where city = 'Delhi'; (to get students only from delhi)
- select * from students where city <> 'Delhi'; (to get students not from delhi)
- select * from students where deptno > 30; (to get students who's deptno > 30)
- multiple condition e.g. AND, OR, NOT: select * from students where deptno > 10 AND city = 'Delhi';
- multiple condition e.g. LIKE, Between, IN, NOT IN:
    - select * from students where name LIKE 'A%';  (to get students with name starting with 'A')
    - select * from students where deptno between 10 and 30; (to get students with deptno 10 to 30 'A')
    - select * from students where city in ('Delhi', 'Jaipur'); (to get students from Delhi and 'Jaipur')


order by
- Examples
    - select * from dept order by dname; (to get dname by Alphabetical Order A to Z)
    - select * from dept order by dname desc; (to get dname by Alphabetical Order Z to A)

group by - To group the rows by using one of the column
    - select city from students group by city;
    - select count(*), city from students group by city;(aggregate function: count(*))
having - used for imposing condition upon group
    - select count(*), city from students group by city having count(*)>=2;
    -  select count(*), city from students group by city;

'''