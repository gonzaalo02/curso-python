###
# 03 . Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

import os
os.system('cls')

# Creación de las listas

print("\nCreación de listas:")

lista1 = [1,2,3,4,5] # lista de enteros
lista2 = ["manzanas", "peras","platanos"] # lista de str
lista3 = [1, "hola", 3.14, True] # lista mixta

lista_vacia = [] # lista vacía
lista_de_listas = [[1,2], [3,4]] # lista de listas
matrix = [[1,2], [3,4], [5,6]] # lista de listas (matriz)

print ("Lista 1:", lista1)
print ("Lista 2:", lista2)
print ("Lista 3:", lista3)
print ("Lista vacía:", lista_vacia)
print ("Lista de listas:", lista_de_listas)
print ("Matriz:", matrix)

# Acceso a elementos por indice

print("\nAcceso a elementos por índice:")
print(lista2[0]) # primer elemento
print(lista2[1]) # segundo elemento
print(lista2[-1]) # último elemento
print(lista2[-2]) # penúltimo elemento

# para acceder a una lista ntro de otra lista
print(lista_de_listas[1][0])

# Slicing (rebanado)

lista1 = [1,2,3,4,5,6,7,8] # lista de enteros

print(lista1[1:4]) # elementos desde el índice 1 hasta el 3
print(lista1[:3]) # primeros tres elementos
print(lista1[3:]) # desde el índice 3 hasta el final
print(lista1[:]) # [copia de toda la lista]

# print(lista1[desde::2]) # elementos desde el índice 0 hasta el final, saltando de 2 en 2
print(lista1[::2]) # elementos desde el índice 0 hasta el final, saltando de 2 en 2
print(lista1[::-1]) # lista invertida

print(lista1)

# Modificar lista

lista1[0] = 10 # cambiar primer elemento
print(lista1)

lista1 = [1,2,3]
lista1 = lista1 + [4,5] # concatenar listas
print(lista1)

# forma mas eficiente de agregar elementos
lista1 += [6,7]
print(lista1)

# Recuperar la longitud de una lista

longitud_lista = len(lista1)
print("Longitud de la lista:", longitud_lista)

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("\nEjercicio 1:")
print(mensaje[7:])


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\nEjercicio 2:")

numero_final_nuevo = numeros[0]
numeros[0] = numeros[-1]
numeros[-1] = numero_final_nuevo

print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

print("\nEjercicio 3:")
sandwich = pan + ingredientes + pan_abajo
print(sandwich)


# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista_duplicada = lista
print(lista_duplicada)

lista += lista_duplicada
print(lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("\nEjercicio 5:")

lista = [10, 20, 30, 40, 50]
centro = lista[len(lista)//2]

print (centro)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]



print("\nEjercicio 6:")
lista = [1, 2, 3, 4, 5, 6]
medio = len(lista)//2
lista_invertida = lista[:medio][::-1] + lista[centro:]
lista_invertida += lista[medio:]
print(lista_invertida)
