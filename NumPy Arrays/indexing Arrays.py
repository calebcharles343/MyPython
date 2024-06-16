import numpy as np

ar1 = np.array([2,4,6,8,10,12,14,16,18,20])

ar2 = np.array([[2,4,6,8],[1,3,5,7],[11,22,33,44],[10,20,30,40]])

print(ar2[0, 0])
print(ar2[-1, -1])

# Slicing
print(ar1[2:9])
print(ar1[2:9:2])

print(ar2[0:2])
print(ar2[0:3:2])

# #######################
print('# #######################')

print(ar2[:,0:2])
print(ar2[0:2,2:4])