import matplotlib.pyplot as mlp

meses=["Enero","Febrero","Marzo","Abril"]
ventas=[1500,1800,1200,2000]
gasto_publicitario=[500,700,400,800]

mlp.bar(meses,ventas, color="skyblue",edgecolor="black")
mlp.title("Ventas de cada mes")
mlp.xlabel("meses")
mlp.ylabel("ventas")
mlp.show()

#2

mlp.plot(meses,ventas, color="darkblue")
mlp.title("Tendencia de las ventas")
mlp.xlabel("meses")
mlp.ylabel("ventas")
mlp.grid(True,color="black")
mlp.show()

#3

mlp.scatter(gasto_publicitario,ventas, color="darkblue", marker="4")
mlp.title("Relacion de gasto y ventas")
mlp.xlabel("gasto_publicitario")
mlp.ylabel("ventas")
#mlp.grid(True,color="black")
mlp.show()