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
# # Para trabajar con regukar expreissions en Python, usamos el módulo `re`
import re
# 
# # 2. Crear un patron, que es una cadena de texto que describe lo que queremos buscar
# 
# pattern = "Hola"
# 
# # 3. El texto que queremos buscar
# text = "Hola mundo"
# 
# # 4. Usar la funcion de busqueda de "re"
# result = re.search(pattern, text) # 
# 
# if result:
#     print("He encontrado el paton en el texto")
# else:
#     print("No he encontrado el patron en el texto")
# 
# 
# # metodos comunes en el modulo re:
# print(result.group()) # Devuelve la parte del texto que coincide con el patrón
# 
# # .start() devolve la posición inicial de la coincidencia
# print(result.start())
# 
# # .end() devuelve la posición final de la coincidencia
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
# text = "Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil. Ojo con Python"
# 
# pattern = "Python" # si ponemos pattern = "Py.hon" tambien encontraria "Python" ya que el punto (.) representa cualquier caracter
# 
# matches = re.findall(pattern, text)
# 
# print(matches)
# 
# print(len(matches)) # numero de coincidencias encontradas
# 
# # ----------------------
# 
# # iter() devuelvemun iterador que contiene todos los resultados de la busqueda
# 
# text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
# pattern = "Python"
# 
# matches = re.finditer(pattern, text)
# 
# for match in matches:
#   print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

pattern = "midu"

result = re.search(pattern, text)
if result:
    print(f"He encontrado el patron en la siguiente posicion {result.start()} hasta la poscion {result.end()}")
else:
    print("No se ha encontrado el patron en el texto")





    