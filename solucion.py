import pandas as pa
from datetime import datetime 
df=pa.read_csv("data/ejercicio.csv",nrows=5) 
print(df)

Año_actual= 2025
df["Edad"] = Año_actual - df["AñoNacimiento"]
fr2= pa.read_csv("data/ejercicio.csv", usecols=["Nombres","Apellidos"])

fr4=["Nombres",'Apellidos','Edad']
df=df[fr4]
print(df)

df.to_excel("miarchivo.xlsx", index="true")