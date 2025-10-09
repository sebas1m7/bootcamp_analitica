import pandas as pa

df=pa.read_json("data/datis.json")
print("Dataframe original:")
print(df)

#filtro por fechas

df["Fechas"]=pa.to_datetime(df["Fechas"],format=("%d/%m/%Y"))
df_filtrado= df[df["Fechas"].between("2000-01-01", "2010-01-01")]
print ("Nueva dateframe")
print (df_filtrado)