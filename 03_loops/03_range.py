###
# 03 - range()
# Permite crear una secuencia de números. Puede ser util para for, pero también para otras cosas.
###

print("\nrange():")

nums = range(10) # No crea una lista, rango del 0 al 5
print(type(nums))
print(nums)


# Una secuencia del 1 al 9, el 10 no esta incluido
for num in range(10):
    print(num)


for num in range(5, 10):
    print(num)


# Tambien lo podemos hacer con numeros negativos
for num in range(-10, 0):
    print(num)

for num in range(10,0,-1):
    print(num)

# Range crea los numeros sobre la marcha, no crea la lista

nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# Tambien para repetir lo mismo x veces

for _ in range(5):
    print("Hola")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

for num in range(1, 11):
    print(num)

numbers = [num for num in range(1, 11)]

for num in numbers:
    print(num)



# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

for num in range(1, 21):
    if num % 2 != 0:
        print(num)



# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

numbers = range(5, 51, 5)
for num in numbers:
    print(num)

for num in range(5, 51, 5):
    print(num)





# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

numbers = range(10, 0, -1)
for num in numbers:
    print(num)

for num in range(10, 0, -1):
    print(num)



# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

suma =0

for num in range(1, 101):
    suma += num

print(f"La suma es: {suma}")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

num = int(input("Introduce un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


