'''def suma(a,b):
    sum=a+b
    return sum
print(suma(7,10))
print(suma(5,11))
print(suma(9,19))

def saluda(nom):
    return print(f"Que se dice {nom}")

saluda("Lucio")
saluda("Fabio")
saluda("Lucas")

def cuadrado(n):
    return n ** 2
numero= cuadrado(2)
print(f"el resultadoes: {numero}")'''

'''def cambia(d,o):
    r=[]
    for i in d:
        if i is None:
            r.append(o)
        else:
            r.append(i)
    return r 
            
datos=[1,None,2,None,3]
print(cambia(datos,0))


cambia2 = lambda datos,p: [p if i is None else i for i in datos]
print(f"cambia con lambda {cambia2(datos,0)}")

suma2= lambda x,y:x+y
print(f"la suma de 4 + 1 es = {suma2(4,1)}")'''

#numeros=[10,8,45,26,7]

'''numeros=[10,8,45,26,7]
numeros.sort()
print("Numeros ordenados:", numeros)

suma_total = sum(numeros)
print("La suma total es:", suma_total)'''

'''numeros=[10,8,45,26,7]

ordenados = sorted(numeros)
suma_total = sum(ordenados)
print("Numeros ordenados:", ordenados)
print("La suma total es:", suma_total)'''

print("suma total:", sum(sorted([10, 8, 45, 26,7])))