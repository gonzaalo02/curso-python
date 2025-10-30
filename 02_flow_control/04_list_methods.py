###
# 04 - Listas métodos
# Los métodos mas importantes para trabajar con listas
###

import os
os.system("cls")

# Añadir o insertar elementos en una lista


lista1 = [1,2,3,4,5]

lista1.append(6) # agrega un elemento al final de la lista
print("Después de append(6):", lista1)

lista1.insert(2, 7) # el primer parametro es el indice del nuevo elemento que vas a insertar, el segundo es el valor

print("Después de insert(2, 3):", lista1)

lista1.extend([8,9,10]) # agrega multiples elementos al final de la lista
print("Después de extend([8,9,10]):", lista1)

# Eliminar elementos de una lista

lista1.remove(3) # elimina el primer 3 que encuentra, no todos los 3 que haya en la lista

print("Después de remove(3):", lista1)

ultimo = lista1.pop() # elimina y retorna el último elemento de la lista
print("Después de pop():", lista1)
print("Elemento eliminado con pop():", ultimo)

lista1.pop(2) # elimina y retorna el elemento en el índice 2
print("Después de pop(2):", lista1)

del lista1[-1] # elimina el último elemento usando del
print("Después de del lista1[-1]:", lista1)

# ELiminar todos los elementos de la lista

lista1.clear() # elimina todos los elementos de la lista
print("Después de clear():", lista1)

# Eliminar un rango de elementos
lista1 = [1,2,3,4,5]
del lista1 [3:] # elimina desde el índice 3 hasta el final
print("Después de del lista1[3:]:", lista1)

# Mas metodos útiles

print("Ordenar listas")
numbers = [3,10,2,8,99,101]
numbers.sort() # Lo que hace es modificar la lista y guarda en la lista la lista ordenada y no la devuelve
print("Después de sort():", numbers)

# Ordenar una lista creando una copia

print("Ordenar una lista creando una copia")
numbers = [3,10,2,8,99,101]
sorted_numbers = sorted(numbers) # sorted() devuelve una nueva lista ordenada
print("Lista original:", numbers)
print("Lista ordenada con sorted():", sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minusculas)")

frutas = ["manzana", "pera", "limón", "manzana", "pera", "limón"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mayusculas y minusculas)")

frutas = ["manzana", "Pera", "Limón", "manzana", "pera", "limón"]
frutas.sort(key=str.lower) # ordena ignorando mayusculas y minusculas
print(frutas)

# Mas metodos útiles

numbers = [1,2,2,3,4,4,5]
print(numbers.count(2)) # cuenta cuantas veces aparece el 2 en la lista
print(5 in numbers) # verifica si el 5 está en la lista, devuelve True o False
print(10 in numbers) # verifica si el 10 está en la lista, devuelve True o False

print("Ordenar una lista de cadenas de texto (todo minusculas)")

frutas = ["manzana", "pera", "limón", "manzana", "pera", "limón"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista_numbers = [1,2,3,4,5]

lista_numbers.append(6)

lista_numbers.insert(2, 10)

lista_numbers[0] = 0

print(lista_numbers)


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a.extend(lista_b)

lista_a.remove(1)

elemento_eliminado = lista_a.pop(3)
print(f"El elemento eliminado ha sido {elemento_eliminado}")

lista_a.clear()

print(lista_a)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista_numbers2 = [1,2,3,4,5,6,7,8,9,10]

del lista_numbers2[2:5]

print(lista_numbers2)


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista_numbers3 = [5, 2, 8, 1, 9, 4, 2]

lista_numbers3.sort()

print(lista_numbers3.count(2))

print(7 in lista_numbers3)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1,2,3]
copia_1 = original[:]

print(copia_1)

copia_2 = original.copy()

print (copia_2)

referencia = original

referencia[0] = 10
print(original)
print(copia_1)
print(copia_2)
print(referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

frutas2 = ["Manzana", "pera", "BANANA", "naranja"]
frutas2.sort(key=str.lower)

print(frutas2)

sorted(frutas2)

print(frutas)


