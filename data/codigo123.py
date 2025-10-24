import pandas as pd
import random
from textblob import  TextBlob
from googletrans import Translator
datos1 = pd.read_csv('eccomers.csv',nrows=1000)
datos1.drop(["Order_Number","Assigned Supervisor"], axis=1, inplace=True)
datos1.dropna(inplace=True)


print(datos1.isnull().sum())
datos1.columns = ["Pais","Nombre_cliente","Datos_pedido","Estado","Producto","Categoria","Marca","Costo","Ventas","Cantidad","Costo_Totales","Ventas_totales"]

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
#marcar=["Dell"."Asus","Sansung","","*"]
dato=input("ingrese la marca que desea buscar:")
filtro=df["Marca"]==dato
print(df[filtro])
