###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

for num in range(2, 21):
    if num % 2 == 0:
        print(num)



# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

suma = 0

for numero in numeros:
    suma += numero

media = suma / len(numeros)
print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

n_max = 0
for numero in numeros:
    if numero > n_max:
        n_max = numero

print(f"El número máximo es: {n_max}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

nueva_lista = []

for palabra in palabras:
    if len(palabra) > 5:
        nueva_lista.append(palabra)

print(f"Palabras con más de 5 letras: {nueva_lista}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower()  # Convertimos la letra a minúscula
contador = 0
for palabra in palabras:
  if palabra.lower().startswith(letra):  # Comparamos en minúsculas
    contador += 1
print(f"Hay {contador} palabras que empiezan con la letra {letra}")

