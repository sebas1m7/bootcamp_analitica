import matplotlib.pyplot as mpl

Productos=["Manzanas","Peras","Naranjas"]
Ventas=[50,80,30]

mpl.bar(Productos, Ventas)
mpl.title("Ventas por producto")
mpl.xlabel("Productos")
mpl.ylabel("Ventas")
mpl.show()