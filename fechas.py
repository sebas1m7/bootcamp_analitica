'''import datetime as dati
import dateutil.relativedelta as rela

fecha_llegada= dati.datetime.now()
print(f"La fecha y hora de llegada: {fecha_llegada}") 

print(fecha_llegada.strftime ("%Y-%mm-%dd"))# strftime se utiliza para la fecha

f1=dati.date(2025,10,5)
f2=dati.date(2025,10,25)
print(f"total de dias: {f1-f2}")
diferencia= f2-f1
print(f"tottal de dias: {diferencia.days}")

f1=dati.date(2001,4,4)
f2=dati.date(2025,10,7)
print(f"total de dias: {f2-f1}")

diferencia= f2-f1
print(f"tottal de dias: {diferencia.days}")

f1=dati.date(2001,4,4)
f2=dati.date(2025,10,7) 

diferencia=rela.relativedelta(f2,f1)
print(f"Años: {diferencia.years}")
print(f"Meses: {diferencia.months}")
print(f"Dias: {diferencia.days}")'''

from datetime import date
from dateutil.relativedelta import relativedelta as rela

def diferencia_fechas(f1,f2)