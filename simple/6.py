import sympy as sp

x, y, z = sp.symbols('x y z')

F = x**2*y + y**2*z**2 + sp.sin(x*z)

Fx = sp.diff(F, x)
Fy = sp.diff(F, y)
Fz = sp.diff(F, z)

J = sp.Matrix([Fx, Fy, Fz])

print("Given Function:")
print(F)

print("\nPartial Derivative w.r.t x:")
print(Fx)

print("\nPartial Derivative w.r.t y:")
print(Fy)

print("\nPartial Derivative w.r.t z:")
print(Fz)

print("\nJacobian Matrix:")
sp.pprint(J)