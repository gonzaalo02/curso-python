###
# 02 - Bucle for
# Permiten ejecutar un bloque de codigo repetidamente mientras ITERA un iterable o una lista
###

import os
os.system("cls")

# Iterar una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

cadena = "midudev"
for letra in cadena:
    print(letra)

# enumerate() para enumerar las propiedades de ka lista
for index, fruta in enumerate(frutas):
    print(f"El indice es {index} y la fruta es {fruta}")

# Bucles anidados un for dntro de otro for

letras = ["a", "b", "c"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}-{numero}")

# Python tutor para ver paso a paso como fuciona un bucle for

# break

animales = ["perro", "gato", "elefante", "tigre", "mono"]

for animal in animales:
    if animal == "tigre":
        break
    print(animal)

for animal in animales:
    if animal == "tigre": continue
    print(animal)

# Compresion de lineas (list comprehensions) con bucles for

animales = ["perro", "gato", "elefante", "tigre", "mono"]
animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)

# Muesra los numeros pares de una lista

pares = [num for num in [1,2,3,4,5,6] if num % 2 == 0]
print(pares)

