###
# 02 - Booleanos
# Valores logicos: True (verdadero) y False (falso)
# Fundamentales para el control de flujo y la lógica en programación.
###

import os
os.system('cls')

# Los booleanos representan valores de verdad: True o False
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación devuelven booleanos
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)       # True
print("5 < 3:", 5 < 3)       # False
print("5 == 5:", 5 == 5)     # True (igaldad)
print("5 != 3:", 5 != 3)     # True (desigualdad)
print("5 >= 5:", 5 >= 5)     # True (mayor o igual)
print("5 <= 3:", 5 <= 3)     # False (menor o igual)

print("\nComparacion de cadenas:")
print("manzana < pera:", "manzana" < "pera")  # True (orden lexicográfico)
print("Hola == hola:", "Hola" == "hola")      # False (sensible a mayúsculas)

# Operadores lógicos combinan booleanos
print("\nOperadores lógicos:")
print("True and False:", True and False)   # False
print("True or False:", True or False)     # True
print("not True:", not True)                 # False
print("not False:", not False)               # True
print("True and True:", True and True)     # True
print("False or False:", False or False)   # False

# Tablas de verdad
print("\nTablas de verdad:")
print("A     B     A and B     A or B    not A")
print("True  True   ", True and True, "     ", True or True, "     ", not True)
print("True  False  ", True and False, "    ", True or False, "    ", not True)
print("False True   ", False and True, "    ", False or True, "    ", not False)
print("False False  ", False and False, "   ", False or False, "   ", not False)