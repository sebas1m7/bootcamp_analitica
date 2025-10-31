"""#1
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

#2.1
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

media = (num1 + num2 + num3) / 3

print(f"La media de los números es: {media}")

#2.2

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso/(estatura**2)

print(f"Tu índice de masa corporal es: {imc:.2f}")

#2.3
horas = float(input("Ingrese el número de horas trabajadas: "))
costo = float(input("Ingrese el costo por hora: "))

pago = horas * costo

print(f"El pago que le corresponde es: {pago}")

#2.4

correctas = int(input("Ingrese el número de respuestas correctas: "))
incorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
blanco = int(input("Ingrese el número de respuestas en blanco: "))

puntaje_final = (correctas * 3) + (incorrectas * -1) + (blanco * 0)

print(f"El puntaje final es: {puntaje_final} ")

#2.5

m = 1
while True:
    try:
        n = int(input())
        if n < 10:
            m *= n
        else:
            break
    except:
        break

print(f"El producto de los números ingresados es: {m}")

#2.6

fibonacci = []
n = int(input("Ingrese el número de elementos de la serie Fibonacci: "))

if n == 0:
    fibonacci = [0, 1]
elif n == 1:
    fibonacci = [0, 1]
else:
    a, b = 0, 1
    for i in range(n):
        fibonacci.append(a)
        a, b = b, a + b

print(f'Los primeros {n} elementos de la serie Fibonacci son: {fibonacci}') 
      
#2.7

inversion = float(input('Ingrese la cantidad a invertir: '))
interes_anual = float(input('Ingrese el interés anual (%): '))
años = int(input('Ingrese el número de años: '))

for i in range(1, años + 1):
    inversion *= (1 + interes_anual / 100)
    
    capital = round(inversion, 2)
    
    if str(capital).endswith('0'):
        print(f'Año {i}: Capital acumulado = {capital:.1f}')
    else:
        print(f'Año {i}: Capital acumulado = {capital:.2f}')

#3.1

matematica = float(input("Ingrese la nota de Matemáticas: "))
fisica = float(input("Ingrese la nota de Física: "))
quimica = float(input("Ingrese la nota de Química: "))
historia = float(input("Ingrese la nota de Historia: "))
lenguaje = float(input("Ingrese la nota de Lenguaje: "))
programacion = float(input("Ingrese la nota de Programacion: "))

print("\nResumen de notas:")
print(f"En Matemáticas has sacado {matematica}")
print(f"En Física has sacado {fisica}")
print(f"En Química has sacado {quimica}")
print(f"En Historia has sacado {historia}")
print(f"En Lenguaje has sacado {lenguaje}")
print(f"En Programacion has sacado {programacion}")

#3.2"""

cesta = {}

while True:
    articulo = input("Ingrese el nombre del artículo (o 'FIN' para finalizar): ")
    if articulo.upper() =="FIN":
        break
    precio = float(input(f"Ingrese el precio de {articulo}: "))
    cesta[articulo] = precio

print("\nLista de la compra: ")
for articulo, precio in cesta.items():
    print(f"{articulo}\t{precio}")

print(f"\nTOTAL\t{sum(cesta.values())}")