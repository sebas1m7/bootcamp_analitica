import math as ma

num=3.9875
truncado = int(num)
redondeado = round(num,0)
print(f"numero truncado: {truncado}")
print(f"numero redondeado: {redondeado}")

print(f"raiz cuadrada de 16: {ma.sqrt(16)}") # sqrt se utiliza para sacar raiz cuadrada
print(f"potencia 4 : {4 ** 2}")  # estas son las dos maneras de sacar la potencia
print(f"potencia con pow {pow(4,2)}")
print(f"logaritmos 100 base 10 {ma.log(100,10)}")

print(f"round hacia arriba {ma.ceil(3.3)}") 
print(f"round hacia abajo {ma.floor(3.9)}") 