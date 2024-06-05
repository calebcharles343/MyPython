task = 'find the birthday of a person'
birthday = {'sachin': '03/14/2003','carl': '01/17/2001','khan': '12/10/2006','donald': '63/14/2010','rohan': '01/6/2005',
}

name = input('Search birthday')

if name in birthday:
       print(name, 'birth is', birthday[name])
else:
       print('name not found')