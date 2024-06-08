# REGULAR FUNCTION

def miles2km(miles):
    kms = 1.6 * miles
    return print(kms)


miles2km(10)

# LAMBDA FUNCTIONS
k = lambda miles: 1.6 * miles

print(k(10))

add = lambda a, b: a + b
print(add(10,30))

f = lambda a, b: a if a > b else b
print(f(23,50))