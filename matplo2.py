import matplotlib.pyplot as mlp

Meses=["Enero","Febrero","Marzo","Abril"]
Ventas=[120,150,110,200]

mlp.plot(Meses, Ventas, color="blue")
mlp.title("Evolucion de Ventas")
mlp.xlabel("Meses")
mlp.ylabel("Ventas")
mlp.grid(True,color="green")# crear margen
mlp.show()