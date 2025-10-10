import pandas as pa

df=pa.read_json("data/personas2.json")
print("data farme lriginal")
print(df)

df1= pa.json_normalize(df["grupo1"])
df2= pa.json_normalize(df["grupo2"])

print("datos 1 ")
print(df1)
print("datos 2")
print(df2)
df_final=pa.concat([df1,df2],axis=0,ignore_index=True)
print(df_final)
print("Validacion data duplicada:")
print(df_final.duplicated())

#sumtoria de duplicados
print("Total de datos duplicados")
print(df_final.duplicated().sum())

#Verificar duplicado por columnas
print(df_final)
print(df_final.duplicated(subset=["Id","Nombre"]))

#datafarme sin duplicados
df_limpio= df_final.drop_duplicates(keep="last")
print(df_final)
print("Dataset sin duplicados")
print(df_limpio)

#suma edades
print(df_final)
# converti texto en numero
df_final["Edad"]=pa.to_numeric(df_final["Edad"],errors="raise")
print(f"suma de edades {df_final["Edad"].sum()}")