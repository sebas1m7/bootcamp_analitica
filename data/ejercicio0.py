import pandas as pa
import matplotlib.pyplot as mlp

dt = pa.read_csv("data/datos99.csv")
dt.drop(columns=["Venta_ID","Precio Unitario"], inplace=True)
#print(dt.info())

#Agrupar las ventas por "Categoría" y sumar la "Cantidad Vendida".
ventas_categoria= dt.groupby(["Categoría"]).sum(["Cantidad Vendida"]).reset_index()
print(ventas_categoria)

mlp.bar(ventas_categoria["Categoría"], ventas_categoria["Cantidad Vendida"],color="aquamarine",edgecolor="darkblue")
mlp.title("Ventas De Categoria")
mlp.xlabel("Cantidad Vendida")
mlp.ylabel("ventas")
mlp.show()
print(dt.info())