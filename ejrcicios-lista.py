"""Crear una lista de 15 numeros generados aleatoriamente entre 1 y 50 
y mostarar y mostar en una lista los paress e impares; 
adicional si el numero 32 se encuentra en la lista
"""

import random;

conjunto=[]
for t in range(15):
    n=random.randint(1,50)
    conjunto.append(n)
print(conjunto)

par=[h for h in conjunto if not h%2]
print(par)
inpar=[h for h in conjunto if h%2]
print(inpar)
if 32 in conjunto:
    print("Ahi se encuentra ")
else:
    print("No esta")