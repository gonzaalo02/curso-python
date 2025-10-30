
###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

import os
os.system("cls")

n1 = input("Introduce un numero\n")
n2 = input("Introduce otro numero\n")

if n1 > n2:
    print(f"El numero {n1} es mayot que {n2}")
else:
    print(f"El numero {n2} es mayor que {n1}")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num1 = float(input("Introduce el primer numero:"))
num2 = float(input("Introduce el segundo numero:"))
operacion = input("Introduce la operacion (+, -, *, /):")
resultado = 0

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2 if num2 != 0 else "Error: Division entre cero"
else:
    print("Operacion no valida")

print(f"El resultado es: {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = int(input("Introduce un año:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"El año {year} es bisiesto")
        else:
            print(f"El año {year} no es bisiesto")
        
