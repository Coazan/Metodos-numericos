from prettytable import PrettyTable
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
tabla = PrettyTable()

iteracion = 0
xa = float(input("Valor inicial: "))
er = 1
a = float(input("Valor intervalo a: "))
b = float(input("Valor intervalo b: "))
b1 = b
xf=0

x = symbols("x")
funcion = sympify(exp((-x-1))*sin(x)-1)  # Aqui se inserta la ecuacion original
f = lambdify(x, funcion)
gx = sympify(exp((-x-1))*sin(x)-1)  # Aqui se inserta la ecuacion despejada
fgx = lambdify(x, gx)
dx = diff(gx, x)
fdx = lambdify(x, dx)


def error(x):
    return 0.5 * 10 ** (2 - x)


error = error(float(input("Cifras significativas: ")))

if f(a) * f(b) < 0:
    tabla.field_names = ["x0", "xf","er","iteracion"]
    while er > error:
        iteracion += 1
        xf = fgx(xa)
        er = abs((xf - xa) / xf)
        tabla.add_row([xa, xf, er, iteracion])
        xa = xf

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
