import pandas as pa

#cargar archivo .csv

df=pa.read_csv("data/dati.csv", sep=";")#, names=['Producto', 'Precio','Cantidad']) 
#si esta con ; en el archivo utilizar sep=";" eje ("data/dati.csv", sep=";")

#mostar la data del cvs
print(df)
print(df.head(2))

df["Precio_total"] = df["Precio"]* df["Cantidad"]
print(df)

# importar columnas especificas csv
fr2= pa.read_csv("data/dati.csv", sep=";", usecols=["Producto","Precio"])

print("Nuevo data farme con dos columnas")
print(fr2)

#importar filas
fr3=pa.read_csv("data/dati.csv", sep=";", nrows=2)# para cambiar el tipo de formato enconding=utf-8
print("Nuevo data frame solo con dos filas")
print(fr3)

df.to_csv("nuevo_archivo.csv", index=False)
df.to_excel("archivo_excel2.xlsx", index=False)