import pandas as pa

df=pa.read_json("data/personas.json")
#print(df)

#Normalizacion de data
df_normalizado=pa.json_normalize(df["estudios"])
print(df_normalizado)

df_final=pa.concat([df.drop(columns="estudios"),df_normalizado],axis=1)
print(df_final)