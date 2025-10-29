###
# 01 -print()
# El modulo print() es el modulo que nos permite imprimir en consola.
# Sirve para mostrar información en consola y te va a compañar
# TODA tu vida. Desde hoy hasta el fin de los tiempos.
###

print("!Hola mundo!")
print('Esto tambien funciona con comillas simples.')

# imprimir varios valores
print("Python", "es", "genial") # por defecto separa con un espacio

print("Python", "es", "genial", sep="-") # cambiar el separador

# por defecto print() añade un salto de linea al final
print("Esto se imprime", end="")
print(" en la misma linea.")

# tambien podemos cambiar el final
print("Esto se imprime", end="!")

# imprimir numeros
print(42)