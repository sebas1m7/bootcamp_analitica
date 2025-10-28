import pandas as pa
ventas = "https://drive.google.com/uc?export=download&id=1txHNdJmFQqfGr1p7_9Y07HjfaHV7oJ1b"
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
print(df_combinado.head(10))
