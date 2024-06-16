import numpy as np

'''
# ONE DIMENSIONAL ARRAY
ar = np.array(12)
print(ar)

ar1 = np.array([1, 2, 3, 4, 5])
print(ar1)

# TWO DIMENSIONAL ARRAY
ar2 = np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])
print(ar2)

# THREE DIMENSIONAL ARRAY
ar3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(ar3)
'''
ar1 = np.array([1, 3, 5, 7, 9])
ar2 = np.array([[1, 2, 3], [4, 5, 6]])
ar3 = np.array([[[1, 1],[2, 2]], [[3, 3], [4, 4]]])
ar4 = np.array([1, 2, 3, 4], ndmin=4)

print(ar1.ndim)
print(ar1.dtype)
print(ar1.itemsize)

print(ar3.shape)
print(ar4.shape)

# ##########################################
print('#### DEMO ####')

ar5 = np.array([1,3,5,7,9])
print(ar5.ndim)

ar5 = np.array([1,3,5,7,9], ndmin=3)
print(ar5.ndim)


