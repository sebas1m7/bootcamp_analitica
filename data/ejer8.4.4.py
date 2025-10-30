import pandas as pa
import matplotlib.pyplot as mlp
import seaborn as sbn

"""url= " https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pa.read_csv(url)
print(df.head(10))

estadisticas= df.groupby("Categoría")["Cantidad Vendida"].sum(['mean', 'median', 'std', 'min', 'max'])
print(estadisticas)"""

url= " https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pa.read_csv(url)
print(df.head(10))

ventasP= df.groupby("Producto").size().reset_index(name="conteo")
print("\n Ventas por producto: ")
print(ventasP)
print(f"\n Cantidad Total: {len(df)}")
mlp.figure (figsize=(12,6))
sbn.barplot(x="Producto", y="conteo", data=ventasP, palette="viridis")
mlp.title("Cantidad de ventas por producto")
mlp.xlabel("Producto")
mlp.ylabel("Cantidad de ventas")    
mlp.tight_layout()
mlp.show()