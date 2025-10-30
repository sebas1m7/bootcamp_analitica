import pandas as pd
import random

datos1 = pd.read_csv('eccomers.csv', nrows=1000)
datos1.dropna(inplace=True)

print(datos1.isnull().sum())
datos1.columns = ["Numero Orden", "Pais", "Nombre_cliente", "Datos_pedido", "Estado", "Producto", "Categoria", "Marca", "Costo", "Ventas", "Cantidad", "Costo_Totales", "Ventas_totales", "Supervisor"]

date = pd.DataFrame(datos1)
date["Ganancias"] = date["Ventas"] - date["Costo"]
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

busqueda = input("¿Desea buscar por Marca o por Supervisor?: ")

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
        print(f"❌ERROR para encontar el supervisor ❌'{dato1}'")

else:
    print("❌Opción no válida. Por favor elija 'Marca' o 'Supervisor❌")