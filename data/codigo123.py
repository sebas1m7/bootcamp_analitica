import pandas as pd
import random
from textblob import  TextBlob
from googletrans import Translator
datos1 = pd.read_csv('eccomers.csv',nrows=1000)
#datos1.drop(["Order_Number","Assigned Supervisor"], axis=1, inplace=True)
datos1.dropna(inplace=True)


print(datos1.isnull().sum())
datos1.columns = ["Order_Number","Pais","Nombre_cliente","Datos_pedido","Estado","Producto","Categoria","Marca","Costo","Ventas","Cantidad","Costo_Totales","Ventas_totales","Supervisor"]

date = pd.DataFrame(datos1)
date["Ganancias"] = date["Ventas"] - date["Costo"]
date["Ganancias_Totales"] = date["Ventas_totales"] - date["Costo_Totales"]
date["Pais"] = [random.choice(["Mexico", "Colombia", "China", "Reino Unido", "Alemania", "Italia", "Francia", "E.E.U.U", "Australia", "India", "Brasil","Japon"]) for i in range(len(date))]
#print(date.head())

df = date
traduciones = {
        'Delivered': 'Entregado',
        'Processing': 'En proceso',
        'Shipped': 'Enviado',
        'Order': 'Pedido'
}
df["Estado"] = df["Estado"].map(traduciones).fillna(df["Estado"])

#print(df.isnull().sum())
#print(df.info())
print(df["Estado"])
#print(df.info())
busqueda = input("¿Desea buscar por Marca o por Supervisor?: ")
if busqueda.lower() == "marca":
                marcas_disponibles = df["Marca"].unique().tolist()
                print("Marcas disponibles:")
                for marca in marcas_disponibles:
                        
                        print("-", marca)
                        dato = input("Ingrese la marca que desea buscar: ")
                        filtro = df["Marca"] == dato
                        resultados = df[filtro]
                        if not resultados.empty:
                                print(f"Resultados para la marca '{dato}':")
                                print(resultados)
elif busqueda.lower() == "supervisor":
                supervisor = df["Supervisor"].unique().tolist()
print("supervisor disponibles:")
for super in supervisor:
                print("-", super)
                dato1 = input("Ingrese la supervisor que desea buscar: ")
                filtro = df["Supervisor"] == dato1
                resultados1 = df[filtro]
                if not resultados.empty:
                        print(f"Resultados para el supervisor '{dato1}':")
                        print(resultados1)
                        
                        
        
       
        
        
                
        '''supervisor = df["Supervisor"].unique().tolist()
        print("supervisor disponibles:")
        for super in supervisor:
        print("-", super)
        dato1 = input("Ingrese la supervisor que desea buscar: ")
        filtro = df["Supervisor"] == dato1
        resultados1 = df[filtro]
        if not resultados.empty:
                print(f"Resultados para el supervisor '{dato1}':")
                print(resultados1)'''