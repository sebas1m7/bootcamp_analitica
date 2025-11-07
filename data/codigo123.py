import pandas as pd
import random

datos1 = pd.read_csv('eccomers.csv')
datos1.dropna(inplace=True)
datos1.drop(["Customer_Name","Cost","Sales"], axis=1, inplace=True)
print(datos1.isnull().sum())

datos1.columns = ["Numero Orden", "Pais", "Datos_pedido", "Estado", "Producto", "Categoria", "Marca", "Cantidad", "Costo_Totales", "Ventas_totales", "Supervisor"]
print(datos1.info())

date = pd.DataFrame(datos1)
date["Ganancias_Totales"] = date["Ventas_totales"] - date["Costo_Totales"]
date["Pais"] = [random.choice(["Mexico", "Colombia", "China", "Reino Unido", "Alemania", "Italia", "Francia", "E.E.U.U", "Australia", "India", "Brasil", "Japon"]) for i in range(len(date))]

df = date
traduciones = {
    'Delivered': 'Entregado',
    'Processing': 'En proceso',
    'Shipped': 'Enviado',
    'Order': 'Pedido'
}
df["Estado"] = df["Estado"].map(traduciones).fillna(df["Estado"])

busqueda = input("¿Desea buscar por Marca o por Supervisor o por pais?: ")

if busqueda.lower() == "marca":
    marcas_disponibles = df["Marca"].unique().tolist()
    print("Marcas disponibles:")
    for marca in marcas_disponibles:
        print("-", marca)
    
    dato = input("Ingrese la marca que desea buscar: ")
    filtro = df["Marca"].str.lower().str.contains(dato.lower())
    resultados = df[filtro]
    
    if not resultados.empty:
        print(f"Resultados para la marca '{dato}':")
        print(resultados)
    else:
        print(f"No se encontraron resultados para la marca '{dato}'")

elif busqueda.lower() == "supervisor":
    supervisores_disponibles = df["Supervisor"].unique().tolist()
    print("Supervisores disponibles:")
    for super in supervisores_disponibles:
        print("-", super)
    
    dato1 = input("Ingrese el supervisor que desea buscar: ")
    filtro = df["Supervisor"].str.lower().str.contains(dato1.lower())
    resultados1 = df[filtro]
    
    if not resultados1.empty:
        print(f"Resultados para el supervisor '{dato1}':")
        print(resultados1)
    else:
        print(f"ERROR para encontar el supervisor '{dato1}'")
elif busqueda.lower() == "pais":
    pais_disponibles = df["Pais"].unique().tolist()
    print("productos disponibles por pais:")
    for pa in pais_disponibles:
        print("-", pa)
    
    dato2 = input("Ingrese el pais que desea buscar: ")
    filtro = df["Pais"].str.lower().str.contains(dato2.lower())
    resultados2 = df[filtro]
    
    if not resultados2.empty:
        print(f"Resultados para el pais '{dato2}':")
        print(resultados2)
    else:
        print(f"ERROR para encontar el pais '{dato2}'")
        
else:
    print("Opción no válida. Por favor elija 'Marca' o 'Supervisor")

df1=df.to_excel('eccolas.xlsx', index=False)
