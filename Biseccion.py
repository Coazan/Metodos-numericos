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
xf = float(input("Valor final: "))


x = symbols("x")
funcion = sympify(input("Inserte funcion: "))
f = lambdify(x, funcion)


def error(x):
    return 0.5 * 10 ** (2 - x)


error = error(float(input("Cifras significativas: ")))

if f(a) * f(b) < 0:
    tabla.field_names = ["x0", "xf", "xr", "er", "iteracion"]
    while er > error:
        iteracion += 1
        xr = (x0 + xf) / 2
        er = abs((xr - xa) / xr)
        tabla.add_row([x0, b, xr, er, iteracion])
        if f(xr) * f(x0) < 0:
            xf = xr
        else:
            x0 = xr

        xa = xr
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
