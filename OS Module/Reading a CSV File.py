# CSV: comma separated values
import csv

f = open('Employees.csv', 'r')
csv_reader = csv.reader(f) # list format
# print(csv_reader)
next(csv_reader)  # get rid of string rows
salaries = []
for row in csv_reader:
    salaries.append(int(row[2]))
print(salaries)

f.close()
