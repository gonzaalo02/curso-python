###
# 04- Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados
###

import os
os.system("cls")

# ejemplo tipico de diccionario


persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

# Para acceder a los valores

print(persona["nombre"])  # midudev
print(persona["calificaciones"][2])  # 9
print(persona["socials"]["twitter"])  # @midudev

# Cambiar valores

persona["edad"] = 26
print(persona["edad"])  # 26

persona["calificaciones"][2] = 10
print(persona["calificaciones"][2])  # 10

print(persona)

# para eliminar una propiedad
del persona["edad"]
print(persona)

es_estudiante = persona.pop("es_estudiante")
print(es_estudiante)  # True
print(persona)

# Metodo update para sobreescribir un diccionario con otro

a = {"nombre": "midudev", "edad": 25}
b = {"edad": 26, "es_estudiante": True}

a.update(b)
print(a)  # {'nombre': 'midudev', 'edad': 26, 'es_estudiante': True}

# Comprobar si existe una propiedad

print("nombre" in persona)  # True
print("edad" in persona)  # False

# metodo para obtener todas las claves
print("\nClaves y valores del diccionario persona:")
print(persona.keys())  # dict_keys(['nombre', 'calificaciones', 'socials'])

# obtener todos los valores
print("\nValores del diccionario persona:")
print(persona.values())  # dict_values(['midudev', [7, 8, 10], {'twitter': '@midudev', 'instagram': '@midudev', 'facebook': 'midudev'}])

# obtener todas las claves
print("\Items")
print(persona.items())

for key, value in persona.items():
    print(f"{key}: {value}")

    