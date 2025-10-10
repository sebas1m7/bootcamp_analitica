import matplotlib.pyplot as mlp

Ingresos=[250,120,570,815,555]
Gastos=[333,160,300,220,400]

mlp.scatter(Gastos,Ingresos, color="darkblue")
mlp.title("Gastos vs Ingresos")
mlp.xlabel("Gastos")
mlp.ylabel("Ingresos")
mlp.show()
