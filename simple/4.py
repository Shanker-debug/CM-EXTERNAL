import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)

eq = sp.Eq(sp.diff(y,x), (x+y)/(x-y))

sol = sp.dsolve(eq, y)

print("Given Differential Equation")
sp.pprint(eq)

print("Solution")
sp.pprint(sol)