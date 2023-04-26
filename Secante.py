from prettytable import PrettyTable
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
tabla = PrettyTable()

er = 1
iteracion = 0
xr = 0
a = float(input("Valor intervalor a: "))
b = float(input("Valor intervalo b: "))
x0 = float(input("Valor inicial: "))
b1=b

encabezado1="x0"
encabezado2="xf"
encabezado3="xr"
encabezado4="error"
encabezado5="iteracion"

x = symbols("x")
funcion = sympify(input("Inserte funcion: "))
f = lambdify(x, funcion)


def error(x):
    return 0.5 * 10 ** (2 - x)

error = error(float(input("Cifras significativas: ")))
if f(a) * f(b) < 0:
    tabla.field_names = ["x0", "xf","xr","er","iteracion"]
    while er > error:
        iteracion += 1
        xr = x0-((b-x0)/(f(b)-f(x0)))*f(x0)
        er = abs((xr - b) / xr)
        tabla.add_row([x0, b, xr, er, iteracion])
        x0=b
        b=xr
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
