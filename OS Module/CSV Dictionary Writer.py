import csv

covid = [
    {'Country': 'India', 'Doses': '18Cr', 'People': '84.1Cr', 'Percentage': 61},
    {'Country': 'China', 'Doses': '330Cr', 'People': '124Cr', 'Percentage': 88.1},
    {'Country': 'United States', 'Doses': '56.8Cr', 'People': '21.9Cr', 'Percentage': 66.4},
    {'Country': 'Brazil', 'Doses': '42.4Cr', 'People': '16.2Cr', 'Percentage': 76.4},
    {'Country': 'Indonesia', 'Doses': '39Cr', 'People': '16.2Cr', 'Percentage': 59.3}
]

file = open('CovidDict.csv', 'w', newline='')  # newline='': Remove space between rows

# file_writer = csv.DictWriter(file, ['Country', 'Doses', 'People', 'Percentage'])
# ['Country', 'Doses', 'People', 'Percentage'] : As headers

# OR

fields = ['Country', 'Doses', 'People','Percentage']
file_writer = csv.DictWriter(file, fields)  # fields : As headers

file_writer.writeheader()  # to write down the headers provided

for d in covid:
    file_writer.writerow(d)

file.close()
