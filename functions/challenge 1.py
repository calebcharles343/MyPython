# check if the maximum difference between two numbers <= 5


def diff(a,b):
    if abs(a - b) <= 5:
        print(True)
    else:
        print(False)


diff(6,9)
diff(-6,-9)