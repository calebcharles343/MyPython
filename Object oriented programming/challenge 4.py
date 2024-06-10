# Instance and class variable

class Employee:
    employee_count = 101

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.emp_id = 'e' + str(Employee.employee_count)
        self.designation = designation
        Employee.employee_count += 1


    def show_details(self):
        print('Name:', self.emp_id)
        print('Employee ID:', self.name)
        print('Designation:', self.designation)
        print('Salary:', self.salary)

    @classmethod
    def total_emp(self):
        return self.employee_count - 101


e1 = Employee('Roi Wesley', '$4000',  'Developer')
e1.show_details()
print('Total Employees', e1.total_emp())
print(' ')

e2 = Employee('Christopher Iliyas', '$100000', 'Developer')
e2.show_details()
print('Total Employees', e2.total_emp())

print(' ')
e3 = Employee('Charles Caleb', '$50000', 'Developer')
e3.show_details()
print('Total Employees', e3.total_emp())
