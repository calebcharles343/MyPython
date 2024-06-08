# calculator

class InvalidFormulaException(Exception):
    pass


def evaluate(formula):
    f = formula.split()
    if len(f) < 3:
        raise InvalidFormulaException('Formula should have spaces eg: 10 + 10')

    if f[1] == '+' or f[1] == '-' or f[1] == '*' or f[1] == '/':
        n1 = int(f[0])
        n2 = int(f[2])
        if f[1] == '+':
            res = n1 + n2
        if f[1] == '-':
            res = n1 - n2
        if f[1] == '*':
            res = n1 * n2
        if f[1] == '/':
            res = n1 / n2
        return res
    else:
        raise InvalidFormulaException('Formula should be eg: 10 + 10')


try:
    formula = input('Enter the formula eg: 10 + 10')
    print(evaluate(formula))
except InvalidFormulaException as e:
    print(e)
