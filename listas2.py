import random;

frutas=["uva","pera","manzana","banano","fresa"]
print(frutas[0]) #accede aprimer elemento de la lista
print(frutas[-1]) #accede al ultimo elemento de la lista
print("_____________")
#recorer toda la lista elemento por elemento
for elemento in frutas:
    print(elemento)
#eleminar la manzana
print("_____________")
#del frutas[2]
print(frutas)
if "manzana" in frutas:
    print("Manzana se encuentra en la lista")
else:
    print("Manzana No se encutra en la lista")
print("_________")
#contar elementos de lista
print(f"La lista de frutas contiene {len(frutas)} elementos")
#contar elementos de la lista con nombre menor a 5 letras
f_corta =[f for f in frutas if len(f)<= 4]#<5

f_corta2=[]
for f in frutas:
    if len(f)<= 4:
        f_corta2.append(f)    
    
print(f"La lista cuenta con {len(f_corta)} frutas con nombres cortos")
print(f" las frutas con nombres cortos son: {f_corta}")
n=random.randint(1,10)
print(f"numero aleatorio es {n}")
     
"""Crear una lista de 15 numeros generados aleatoriamente entre 1 y 50 
y mostarar y mostar en una lista los paress e impares; 
adicional si el numero 32 se encuentra en la lista
"""