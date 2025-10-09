import pandas as pa
'''datos= {
    "Nombres":["Lucio", "Fabio", "Claudio"],
    "Edad":[33,25,66],
    "Ciudad":["Bogota","Cali","Medellin"],
    "RH":["O+","AB-","A-"],
    "Estrato": [3,4,2]
}
dataf= pa.DataFrame(datos)
print (dataf)

#print(dataf["RH"])

#print(dataf.loc[0]) #loc es para nombre del indice
#print(dataf.iloc[2]) # iloc a la posicion del indice

filtro= dataf[dataf["Edad"]>=25]
print (filtro)'''
  ''''''''''''''''''''''''

#ejercicio1
'''datos= pa.Series([100,200,300,400,500], index= ["Lunes","Martes","Miercoles","Jueves","Viernes"])

print(pa.DataFrame(datos))
print(datos)

print(datos["Miercoles"])

promedio= datos.mean()
print(promedio)

nueva_serie= datos+50
print(nueva_serie)'''

