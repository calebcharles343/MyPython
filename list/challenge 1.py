task = 'Calculate Salery, weekly working hours given in a list'

work_hours =[int(x) for x in input('Enter work hours in entire week, separated by space').split()]
wage = int(input('Enter hourly wage'))

total_work_hours = sum(work_hours)

salary = total_work_hours * wage

print(salary)

