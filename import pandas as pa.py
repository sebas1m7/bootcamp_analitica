import pandas as pa

datos=pa.DataFrame({
    "Nombre": ["Ana", "Juan", "María", "Carlos"],
    "Edad": [22,30,25,28],
    "Ciudad":["Madrid", "Barcelona", "Valencia", "Sevilla"]
})
print(datos)

kk=datos[datos["Edad"]<25]
print(kk)
datos["Categoría"] = datos["Edad"].apply(lambda x: "Joven" if x < 25 else "Adulto")
print(datos)