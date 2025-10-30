import pandas as pa
import matplotlib.pyplot as mlp
import seaborn as sbn
# ejercicio 2
"""url= "https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pa.read_csv(url)
#print(df.head())
#print(df.info())

df_numeric= df.select_dtypes(include=("number"))
print(df_numeric.tail())

correlacion_matrix= df_numeric.corr()
#print("Matriz de correlacion:")
#print(correlacion_matrix)

mlp.figure (figsize=(10,6))
sbn.heatmap(correlacion_matrix, annot=True, cmap="coolwarm", linewidths=1)
mlp.title("Mapa de calor de la matriz de correlacion")
mlp.tight_layout()
mlp.show()"""

"""url= "https://drive.google.com/uc?export=download&id=1VbrQjDF2Br0tjHHiruUnp-0qmnQwon1I"
df=pa.read_csv(url)
#print(df.head())
#print(df.info())

df["Puntuacion de credito"]= pa.to_numeric(df["Puntuacion de credito"], errors="coerce")
df["Ingreso Mensual"] = pa.to_numeric(df["Ingreso Mensual"], errors="coerce")
df["Region"]=pa.to_numeric (df["Region"], errors="coerce")
print(df.head())

df["Grupo Credito"]= pa.cut(df["Puntuacion de credito"], bins=[0,300,600,700,800,900], labels=["Malo","Regular","Bueno","Muy Bueno","Excelente"])
print(df.head())
mlp.figure (figsize=(14,6))
sbn.boxplot(x="Grupo Credito", y="Ingreso Mensual",data=df, palette="Set2")

sbn.swarmplot(x="Grupo Credito", y="Ingreso Mensual",data=df, color="0.25")

mlp.title("Puntuacion de credito vs Ingreso Mensual")
mlp.xlabel("Puntuacion de credito")
mlp.ylabel("Ingreso Mensual")
mlp.tight_layout()
mlp.show()"""

# ejercicio 5

#url= " https://drive.google.com/uc?export=download&id=1VbrQjDF2Br0tjHHiruUnp-0qmnQwon1I"
df=pa.read_excel("data/datos_comparacion17.xlsx")
#print(df.info())
df["Puntuacion de credito"]= pa.to_numeric(df["Puntuacion de credito"], errors="coerce")
df["Ingreso Mensual"] = pa.to_numeric(df["Ingreso Mensual"], errors="coerce")
#print(df.isnull().sum())

df["Grupo Edad"] = pa.cut(
    df["Edad"],
    bins=[18, 31, 50,51],
    labels=["Menores", "Adultos", "Mayores"]
)

"""def clasiicar_edad(edad):
    if 18 <= edad <= 30:
        return "Joven"
    elif 31 <= edad < 50:
        return "Adulto"
    elif edad > 50:
        return "mayores"
    
df["Nueva columna"] = df["Edad"].map(clasiicar_edad)
df["Categoria Edad"]= df["Edad"].apply(clasiicar_edad)

df= df[df["Grupo Edad"] != "Fuera de rango"]"""
print(df.head())

mlp.figure(figsize=(10, 6))

sbn.kdeplot(data=df, x="Ingreso Mensual", hue="Grupo Edad", fill=True, common_norm=False, alpha=0.5,
            palette=["darkblue", "green", "orange"])

mlp.title("Distribución del Ingreso Mensual por Grupo de Edad")
mlp.xlabel("Ingreso Mensual")
mlp.ylabel("Densidad")
mlp.tight_layout()
mlp.show()
