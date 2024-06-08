import Student,pickle
with open('student.data', 'rb') as file:
    for data in range(3):
        stud = pickle.load(file)
        stud.close()