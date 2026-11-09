import numpy as np

A = np.array([[1,2], 
     [3,4]])

det = np.linalg.det(A)

print("Matrix:")
print(A)

print("Determinant: ", round(det))

if(abs(det) < 1e-10):
    print("Non-trivial Solution")
else:
    print("Trivial Solution")
    print("Solution: x = 0, y = 0")