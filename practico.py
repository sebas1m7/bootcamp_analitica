#1
numero = float(input("Ingrese un número: "))
print("¿El número está en el rango de 10 a 20?", 10 <= numero <= 20)

# 2
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")

#3
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

if cadena1 == cadena2:
    print("¿Las cadenas son iguales? True")
else:
    print("¿Las cadenas son iguales? False")
    
#4
tamaño = float(input("Ingrese el tamaño del tornillo en centímetros: "))
if tamaño < 1:
    print("Tamaño no valido.")
elif tamaño <= 3:
    print("El tornillo es pequeño.")
elif tamaño <= 5:
    print("El tornillo es mediano.")
elif tamaño <= 6.5:
    print("El tornillo es grande.")
elif tamaño <= 8.5:
    print("El tornillo es muy grande.")
else:
    print("El tornillo es gigante.")
    
#5
lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

# Determinar el tipo de triángulo
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")

#6
e=int(input("Ingrese la Cantidad de empleados: "))
total_sueldos=0
c1=0
c2=0
for i in range(e):
    sueldo=float(input("Ingrese el sueldo del empleado: "))
    if sueldo <=300:
        c1 += 1
        total_sueldos +=300
    else:
        c2 +=1
        total_sueldos +=500
print("Empleados que cobran entre $100 y $300:",c1)
print("Empleados que cobran mas de $300:",c2)
print("Gasto total de sueldos:",total_sueldos)

#7
