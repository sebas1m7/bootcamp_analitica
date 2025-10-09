import pandas as pa

datos={
    "Productos":["Manzana","Banana","Cereza"],
    "Precio": [2.5,1.8,3.0],
    "Cantidad": [10,15,8]
}
dfr= pa.DataFrame(datos)
print("Primeras dos filas")
#print(dfr.iloc[0:2])
print(dfr.head(2))
 
valor_total =(dfr["Precio"]) * (dfr["Cantidad"]).sum()
print("suma total de todo:", valor_total)

#dfr["Precio total"] = dfr["Precio"] * dfr["Cantidad"]
#print(dfr)

#dfr_ordenado= dfr.sort_values(by="Productos", key=lambda x: x.str.lower(), ascending=False)
#print("el data frame ordenadoes:")
#print(dfr_ordenado)