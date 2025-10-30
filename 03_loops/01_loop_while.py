###
# 01 - bucle while
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

import os
os.system("cls")

print("\n Bucle while:")

# Bucle con una simple condicion
contador = 0

while contador <=5:
    print(contador)
    contador += 1

# Bucle infinito

"""
    while True:
        print("Hola")
"""

# para salir de un bucle existe la palabra break

contador = 0

while True:
    print("Hola")
    contador+= 1
    if contador == 5:
        break # sale del bucle


# Tanbien tenemos Continue, que lo que hace es saltar esa iteracion en concreto

contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)


# Else, esta condicion cuando se ejeuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
    contador += 1
    print(contador)
else:
    print("El bucle ha terminado")

# El else no se ejecuta si se ha utilizado break

# pedirle al usuario un número que tiene que ser positivo si no, no le dejamos en paz

# Con try Except para comprobar que no nos pasan un str en vez de numero que rompa el contrato

numero = -1
while numero <= 0:
    try:
        numero = int(input("Escribe un numero positivo: "))
    except:
        print("Lo que introduces debe de ser un numero")
    if numero < 0:
        print("El numero debe ser positivo. Intenta de nuevo")

print(f"EL numero que has introducido es {numero}")

