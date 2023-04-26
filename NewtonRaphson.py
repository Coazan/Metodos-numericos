from prettytable import PrettyTable
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
tabla = PrettyTable()

er = 1
iteracion = 0
xr = 0
xa = 0
a = float(input("Valor intervalor a: "))
b = float(input("Valor intervalo b: "))
x0 = float(input("Valor inicial: "))

x = symbols("x")
funcion = sympify(input("Inserte funcion: "))
f = lambdify(x, funcion)
dx = diff(funcion, x)
fdx = lambdify(x, dx)


def error(x):
    return 0.5 * 10 ** (2 - x)


error = error(float(input("Cifras significativas: ")))

if f(a) * f(b) < 0:
    tabla.field_names = ["x0", "xr", "er", "iteracion"]
    while er > error:
        iteracion += 1
        xr = (x0 - (f(x0) / fdx(x0)))
        er = abs((xr - xa) / xr)
        tabla.add_row([x0, xr, er, iteracion])
        xa = xr
        x0 = xr

    print(tabla)

else:
    print("No hay raiz")

x = np.linspace(-5, 5, 100)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
