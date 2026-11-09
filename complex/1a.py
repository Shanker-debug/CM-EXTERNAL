import numpy as np

A = np.array([[2,1],
             [1,1]])

B = np.array([5,3])

if(np.linalg.det(A) != 0):
    X = np.linalg.solve(A, B)

    print("Unique Solution")
    print("x=", X[0])
    print("y=", X[1])

    AX = A @ X

    print("Verification:")
    print("A@X=", AX)
    print("B=", B)

    residual = B - AX

    print("Residual=", residual)
else:
    print("No unique solution")