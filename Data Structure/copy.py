import copy
'''
# Copy : create duplicates of exiting elements

copy.copy(x) 
copy.deepcopy(x)

l = [10, 20, 30, 40, 50]
l1 = copy.copy(l)  # shallow copy of l means l1 uses the same object as l in memory 
l2 = copy.deepcopy(l)  # deep copy of l means l2 uses new object different from l in memory 

# Note deepcopy() does not work with data types int, float, str
'''



