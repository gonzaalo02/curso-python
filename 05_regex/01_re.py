# ###
# # o1 . Expresiones regulares
# ###
# 
# """ ¿Por qué aprender Regex?
# 
# - Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)
# 
# - Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.
# 
# - Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
# """
# 
# # Para trabajar con regular expreissions en Python, usamos el módulo `re`
import re
# 
# # 2. Crear un patron, que es una cadena de texto que describe lo que queremos buscar
# 
# pattern = "Hola"
# # # 
# # # # 3. El texto que queremos buscar
# text = "Hola mundo"
# # # 
# # # # 4. Usar la funcion de busqueda de "re"
# result = re.search(pattern, text) 

# # 
# if result:
#     print("He encontrado el paton en el texto")
# else:
#     print("No he encontrado el patron en el texto")
#  
# # 
# # # metodos comunes en el modulo re:
# print(result.group()) # Devuelve la parte del texto que coincide con el patrón
# # 
# # # .start() devolve la posición inicial de la coincidencia
# print(result.start())
# #
# # # .end() devuelve la posición final de la coincidencia
# print(result.end())
# 
# # EJERCICIO 01
# # Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# # e indica en que posición empieza y termina la coincidencia.
# 
# text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
# pattern = "IA"
# result = re.search(pattern, text)
# 
# if result:
#     print(f"He encontrado el patron en el texto en la posicion {result.start()} hasta la posicion {result.end()}")
# else:
#     print("No he encontrado el patron en el texto")
# 
# # --------------
# 
# # vamos a encontrar todas las coincidencias de un patron en un texto
# 
#text = "Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil. Ojo con Python"
## 
#pattern = "Python" # si ponemos pattern = "Py.hon" tambien encontraria "Python" ya que el punto (.) representa cualquier caracter
## 
#matches = re.findall(pattern, text)
## 
#print(matches)
## 
#print(len(matches)) # numero de coincidencias encontradas
# 
# # ----------------------
# 
# # iter() devuelve un iterador que contiene todos los resultados de la busqueda
# 
#text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
#pattern = "Python"
## # 
#matches = re.finditer(pattern, text)
## # 
#for match in matches:
#  print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

pattern = "midu"

result = re.search(pattern, text)

matches = re.finditer(pattern, text)

result2 = re.findall(pattern, text)

if result:
    print(f"He encontrado {len(result2)} ocurrencias de la palabra {pattern}")
else:
    print(f"No he encontrado ninguna ocurrencia de la palabra {pattern} ")

for match in matches:
   print(match.group(), match.start(), match.end())



## Modificadores

# Los modificadores son opciones que se pueden agregar a un patron para cambiar su comportamiento

# re.IGNORECASE: ignora las mayusculas y las minusculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no estan mala. Viva la ia"

pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found:
    print(f"He encontrado el patron {found} en el texto.")
    print(f"Se encotro {len(found)} veces")
else:
    print("No he encontrado el patron en el texto")

# Ejercicio 
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minusculas.
print("\nEjercicio 03: ")

text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON es genial."

pattern = "python"

matches = re.findall(pattern, text, re.IGNORECASE)

if matches:
    print(f"He encontrado {len(matches)} ocurrencias de la palabra {pattern}")
else:
    print(f"No he encontrado ninguna ocurrencia de la palabra {pattern} ")

### Remplazar el texto

# .sub() reemplaza todas las coincidencias de un patron en un texto

text = "Hola, mundo. Hola de nuevo"
pattern = "Hola"
replacement = "Adios"

new_text= re.sub(pattern, replacement, text)# Le podemos pasar count(), el numero de veces que queremos reemplazar el patron. Por defecto es 0, que significa todas las ocurrencias. Tambien le podemos pasar flags(), que son los modificadores.


print(new_text)
