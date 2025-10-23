import pandas as pd
from faker import faker 
#paises=["Colombia, Australia,India,Alemania,Mexico"]
date1=pd.read_csv("eccomers.csv")
#print(date.head())
date=pd.DataFrame(date1)
date["ganancias"]=date["Sales"]-date["Cost"]
date["ganancias totales"]=date["Total_Sales"]-date["Total_Cost"]
date["pais"]=date
print(date["ganancias totales"].head)
df=date.dropna()
print(df)

df.drop(columns="Order_Number")
df.drop(columns="Assigned_Supervisor")

