import Student, pickle
stud = [Student.Student(10, 'john', 'cs'), Student.Student(20, 'Ajay', 'ec'), Student.Student(30, 'chris', 'mc')]
with open('student.data', 'wb') as student:
    for data in stud:
        pickle.dump(data, student)