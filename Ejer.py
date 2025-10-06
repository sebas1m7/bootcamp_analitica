
edad=24
if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar")
else:
    print("Eres menor de edad")
print("Fin del programa")

calificacion = 77
if calificacion >= 90: 
    print ('Tu calificación es A.') 
elif calificacion >= 80: 
    print ('Tu calificación es B.') 
elif calificacion >= 70: 
    print ('Tu calificación es C.')
elif calificacion >= 60: 
    print ('Tu calificación es D.')
else: 
    print ('Tu calificación es F.')
    
nota1  = int (input('inserta nota taller'))
nota2  = int (input('inserta nota tarea'))
nota3  = int (input('inserta nota evaluación'))

suma = (nota1 + nota2 + nota3) / 3
print ( 'su nota es',suma)

 
if suma >= 5: 
    print ('Tu calificación es exelente.') 
elif suma >= 4: 
    print (f'Tu calificación es sobresaliente con {suma}.')
elif suma >= 3: 
    print ('Tu calificación es aceptable.') 
else:
    print('no aprobo la materia')