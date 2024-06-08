# CALLER CLASS
class dept:
    def __init__(self):
        self.depts = {'hr': 'Human Resource',
                      'acc': 'Accounts & finance',
                      'sd': 'Sales & Distribution',
                      'mkt': 'Marketing'}

    def __call__(self, dept):
        return self.depts[dept]


d = dept()
s = d('hr')
print(s)

print('####################################')

# CALLER CLASS CONVERTED TO CLOSURE FUNCTION
def dept2():

    depts = {'hr': 'Human Resource',
             'acc': 'Accounts & finance',
             'sd': 'Sales & Distribution',
             'mkt': 'Marketing'}

    def name(dept):
        return depts[dept]

    return name

d = dept2()
s = d('hr')
print(s)