def f(x):
    return x**3 - 4*x - 9

def df(x):
    return 3*x**2 - 4

x = 3
n = 10

print("Newton Raphson Method")
print("Iteration\troot")

for i in range(n):
    x = x - f(x) / df(x)

    print(i+1, "\t", round(x,6))
print("Real Root: ", round(x,6))