###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares,
###

import re, os
os.system("cls")

# 1. EL punto (.)
# Coincidir con cualquier caracter excepto un salto de linea

text = "Hola mundo. H0la de nuevo. H0la otra vez"
pattern = "H.la" # Coincidir con "Hola", "H0la", etc.

found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No he encontrado ninguna coincidencia")

text = "casa caasa cosa cisa cesa causa"
pattern ="c.sa"

matches = re.findall(pattern, text)

print(matches)

# ---------------------

text = "Hola mundo. H0la de nuevo. H0la otra vez"
pattern = r"H.la" # Coincidir con "Hola", "H0la", etc.

found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No he encontrado ninguna coincidencia")

text = "Mi casa es blanca. Y el coche es negro."

pattern = r"\." # para cancelar el significado de punto y que busque el punto original

matches = re.findall(pattern, text)

print(matches)

# \d : coincide con cualquier digito (0-9)

text = "El numero de telefono es 123456789"

found = re.findall(r"\d{9}", text)

print(found)

# Ejercicio: detectar si hay un numero de España en el texto gracias al prefijo +34

text = "Mi numero de telefono es +34 666666666"

pattern = r"\+34 \d{9}"

found = re.search(pattern, text)

if found: print(f"Encontré el numero de telefono {found.group()}")

# \w: coincide con cualquier caracter alfanumerico (letras y numeros)

text = "gonzalo_02"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)
text = "Hola mundo\n¿Como estas?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el principio de una cadena

username = "@432_name"
pattern = r"^\w" # validar nombre de usuario
found = re.search(pattern, username)

if found: print("El nombre de usuario es valido")
else: print("El nombre de usuario no es valido")

# telefono

text = "+34 666666666" 
pattern = r"^\+\d{2,3} " # todos empieza con + y 2 o 3 digitos. hay un espacio despues del prefijo para separar del numero

valid = re.search(pattern, text)

if valid: print("El telefono es valido")
else: print("El telefono no es valido")

# $: Coincide con el final de una cadena
text = "hola mundo"
pattern = r"mundo$"
valid = re.search(pattern, text)

if valid: print("El texto termina con 'mundo'")
else: print("El texto no termina con 'mundo'")

# Ejercicio: validar un email simple. # Esto no sirviria si hay puntos en el dominio o en el nombre de usuario
email = "gonzalo@gmail.com"
pattern = r"gmail.com$"
valid = re.search(pattern, email)

if valid: print("El email es valido")
else: print("El email no es valido")


# Ejercicio:
# Tenemos una lista de archivos, necesitamos saber los nombres de o¡los ficheros con extensiones .txt
text = "file1.txt file2.pdf gonzalo-of.webp secret.text"

# \b: coincide con el principio o el final de una palabra
text = "casa casada casado"

pattern = r"\bcasa\b"
matches = re.findall(pattern, text) # esto es para que solo coincida con "casa" y no con "casada" o "casado"
print(matches)

# |: Coincider con una opcion u otra
frutas = "platano, manzana, aguacate, pera"
pattern = r"manzana|pera"
matches = re.findall(pattern, frutas)

print(matches)


