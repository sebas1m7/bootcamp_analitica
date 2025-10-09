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