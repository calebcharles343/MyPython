task = 'create dictionary with student details'

student = {}
for i in range(3):
    name = input('Enter name')
    roll = input('Enter roll')
    dept = input('Enter dept')

    student[name] = {'Name': name, 'Roll': roll, 'Dept': dept}
print(student)