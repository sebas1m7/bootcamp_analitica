import pandas as pa
import matplotlib.pyplot as mlt
"""ventas = "https://drive.google.com/uc?export=download&id=1txHNdJmFQqfGr1p7_9Y07HjfaHV7oJ1b"
productos = " https://drive.google.com/uc?export=download&id=1Vbfvur9orXO3lbb9RQgu27hAg1F9BMKm"
df_v=pa.read_csv(ventas)
df_p=pa.read_csv(productos)
print(df_p.head())
print(df_v.head())

df_v.set_index("Producto_ID", inplace=True)
df_p.set_index("Producto_ID", inplace=True)

# Metodo con el merge
#1
#df_combinado= pa.merge(df_v, df_p, left_index=True, right_index=True, how="inner")
#2
df_combinado= pa.merge(df_v, df_p, on="Producto_ID", how="inner")
# Metodo con join
#df_combinado= df_v.join(df_p, how="inner")
#print(df_combinado.head())

df_combinado["Ingresos Totales"]= df_combinado["Cantidad Vendida"] * df_combinado["Precio Unitario"]
print(df_combinado.head(10))"""

# Ejercicio: Cálculo del Precio Unitario Promedio por Categoría 8.7.2
datos1 = " https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df= pa.read_csv(datos1)
print(df.head(10))

#agrupar los datos por columna "Categoria" redondear el valor promedio de la columna "Precio Unitario"
precio_promedio= df.groupby("Categoría")["Precio Unitario"].mean().round(2).reset_index()
print(precio_promedio)

"""mlt.bar(precio_promedio["Categoría"], precio_promedio["Precio Unitario"], color="darkblue", edgecolor="white")
mlt.xlabel("Categoría")
mlt.ylabel("Precio Unitario Promedio")
mlt.title("Precio Unitario Promedio por Categoría")
#mlt.grid(True,color="green")
mlt.tight_layout()
mlt.show()
"""
# Forma 2
precio_promedio.plot(kind="bar", x="Categoría", y="Precio Unitario", legend=False, color="skyblue", edgecolor="black", title="Precio Unitario Promedio por Categoría")
mlt.xticks(rotation=45)
mlt.tight_layout()
mlt.grid(axis="y", linestyle="--", alpha=0.7)
mlt.show()