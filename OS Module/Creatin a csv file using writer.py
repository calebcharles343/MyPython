import csv

covid = [('Country', 'Doses', 'People', 'Percentage'),
         ('India', '18Cr', '84.1Cr', 61),
         ('China', '330Cr', '124Cr', 88.1),
         ('United States', '56.8Cr', '21.9Cr', 66.4),
         ('Brazil', '42.4Cr', '16.2Cr', 76.4),
         ('Indonesia', '39Cr', '16.2Cr', 59.3),
         ]

file = open('Covid.csv', 'w', newline='')  # newline='': Remove space between rows

file_writer = csv.writer(file)

for t in covid:
    file_writer.writerow(t)

file.close()
