import numpy as np
import sympy as sp

A = np.array([[2,1],
              [4,2]])

B = np.array([4,8])

rank_A = np.linalg.matrix_rank(A)
rank_AB = np.linalg.matrix_rank(np.column_stack((A,B)))

num_vars = A.shape[1]

print("Rank of A: ", rank_A)
print("Rank of [A|B]: ", rank_AB)
print("No. of variables: ", num_vars)
print("Degree of freedom: ", num_vars - rank_A)

if(rank_A == rank_AB and rank_A < num_vars):
    print("Infinite solution: True")
else:
    print("Infinite solution: False")

x, y = sp.symbols("x y")

eq1 = sp.Eq(2*x+y, 4)
eq2 = sp.Eq(4*x+2*y, 8)

sol = sp.solve([eq1, eq2], [x, y])
print("Solution: ", sol)