import sympy as sp

n = int(input("Enter the order of the matrix: "))

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

A = sp.Matrix(a)

lam = sp.symbols('lambda')
I = sp.eye(A.rows)

print("Given matrix:")
sp.pprint(A)

B = A - lam * I

print("A - lam * I:")
sp.pprint(B)

poly = B.det()

print("Characteristic Equation:")
sp.pprint(sp.Eq(poly, 0))

print("\nSTEP - 1: FINDING EIGEN VALUES")
eigenvalues = sp.solve(poly, lam)

print("Eigen values: ", eigenvalues)

print("\nSTEP 2: FINDING EIGENVECTORS")

for val in eigenvalues:
    print("For eigenvalue: ", val)

    M = (A - val * I)
    print("Substituting in the (A - lam * I):")
    sp.pprint(M)

    print("solving (A - lam * I)V = 0")

    eigenvectors = M.nullspace()

    print("Eigen Vectors:")
    for vec in eigenvectors:
        sp.pprint(vec)