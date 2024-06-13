'''

Fractions : represents a rational number with a numerator which is greater
and denominator which is greater
'''

'''
# IDLE lines

import fractions
f1 = fractions.Fraction(1,2)
f1 #  Fraction(1, 2)

print('{}'.format(f1))  # 1/2
f2 = fractions.Fraction(0.2)
f2  # Fraction(3602879701896397, 18014398509481984)
f3 = fractions.Fraction('0.3')
f3  # Fraction(3, 10
f2 = f2.limit_denominator(10)  # I.E. denominator not more than 10
f2  # Fraction(1, 5)

#ARITHMETICS
print('{}'.format(f1 + f2))  # 7/10
print('{}'.format(f2 - f1))  # -3/10
print('{}'.format(f2 * f1))  # 1/10
print('{}'.format(f2 / f1))  # 2/5

##################
L = [(1, 2),(4, 9),(6, 8)]
for n,d in L:
        print('{}'.format(fractions.Fraction(n, d)) # 1/2, 4/9, 3/4
'''
