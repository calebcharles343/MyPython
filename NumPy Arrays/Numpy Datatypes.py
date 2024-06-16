import numpy as np

ar1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(ar1.dtype)  # Result = int32: 32/8 = 4bytes. Means each int in array takes 4byte in memory

ar2 = np.array([1.1, 2.1, 3.1, 4.1])

print(ar2.dtype)  # Result = float64: 64/8 = 8bytes. Means each float in array takes 8byte in memory

print('#####################################')

ar3 = np.array([1, 2, 3, 4, 128], 'b')
print(ar3)
print(ar3.dtype)  # Result = int8: range is -128 to 127, mean -129 and 128 triggers an overflow

ar4 = np.array([1, 2, 3, 4, 128], 'B')
print(ar4)
print(ar4.dtype)  # Result = uint8: range is 0 to 255, mean -1 and 256 triggers an overflow

