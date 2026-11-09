import sympy as sp

A = sp.Matrix([[2,1,0],
               [1,2,0],
               [0,0,4]])

print("Eigenvalues and Eigenvectors:")
eigen_data = A.eigenvects()

P_cols = []

for value, mult, vectors in eigen_data:
    print("Eigenvalue= ", value)

    for v in vectors:
        print("Eigenvector:")
        sp.pprint(v)

        u = sp.simplify(v / sp.sqrt((v.T * v)[0]))
        P_cols.append(u)

P = sp.Matrix.hstack(*P_cols)

print("Orthogonal Matrix")
sp.pprint(P)

print("Transpose of P:")
sp.pprint(P.T)

D = sp.simplify(P.T * A * P)

print("Diagonal Matrix:")
sp.pprint(D)

y1, y2, y3 = sp.symbols('y1 y2 y3')
Y = sp.Matrix([y1, y2, y3])

X = sp.simplify(P*Y)

print("Transformation X = PY")
sp.pprint(X)

q1 = sp.simplify((X.T * A * X)[0])
q2 = sp.simplify((Y.T * D * Y)[0])

print("\nOriginal Quadratic Form:")
sp.pprint(q1)

print("\nDiagonal Quadratic Form:")
sp.pprint(q2)

if(sp.simplify(q1 - q2) == 0):
    print("VERIFIED")
else:
    print("NOT VERIFIED")