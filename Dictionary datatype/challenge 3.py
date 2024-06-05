task = 'Create a dictionary for country names in alphabetical order'

eg_countries = {
    'A': ['America', 'Alaska', 'Argentina'],
    'B': ['Bhutan', 'Brazil', 'Bahrain'],
    'C': ['China', 'Costa Rica', 'Cuba'],
}

countries = {}

for i in range(4):
    name = input('Enter Country Name')
    if name[0].upper() not in countries:
        countries[name[0].upper()] = [name]
    else:
        countries[name[0].upper()].append(name)

print(countries)