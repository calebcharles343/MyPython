import numpy as np

ar = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(ar.shape)

arReshape2D = ar.reshape(3,4)

print(arReshape2D)
print(arReshape2D.shape)


arReshape3D = ar.reshape(3,2,2)

print(arReshape3D)
print(arReshape3D.shape)


arFlattened = arReshape3D.flatten()
print(arFlattened)
