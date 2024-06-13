import csv
import pprint

f = open('Employees.csv', 'r')
csv_dictReader = csv.DictReader(f) # dictionary format

employees = {}

for row in csv_dictReader:
    employees[row['Name']] = row
pprint.pprint(employees) # for nice print formating
print('Harry', employees['Harry'])


f.close()