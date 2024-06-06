positional_arguments = 'Example below'


def net_salary(basic, allowance, deduction):
    print('basic', basic)
    print('allowance', allowance)
    print('deduction', deduction)
    net = basic + allowance - deduction
    return print('Net salary is', net)


net_salary(8000, 6000, 2000)

keyword_arguments = 'Example below'

net_salary(deduction = 2000, basic = 12000, allowance = 3000)

mix_arguments = ('when using positional and keyword together, positional'
                 'arguments must always come first')
net_salary(5000, deduction = 2000, allowance = 13000)