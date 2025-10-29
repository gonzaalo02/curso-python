###
# 05 - Entrada de usuario (input()) - Version simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

print("Hola como te llamas?")
nombre = input()  # Solicita al usuario que ingrese su nombre y se guarda en la variable 'nombre'
print(f"Encantado de conocerte, {nombre}!")

# otra forma de hacerlo en una sola línea
nombre = input("Hola como te llamas?\n")  # Solicita al usuario que ingrese su nombre
print(f"Encantado de conocerte, {nombre}!")

# Solicitar al usuario su edad
age = input("¿Cuántos años tienes?\n")
age = int(age)  # Convertir la entrada de texto a un número entero
print(f"¡Tienes {age} años!")

print("obtener multiples valores a la vez")
country, city = input("¿En que pais y ciudad vives?\n").split()  
print(f"Vives en {city}, {country}.")

