###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones.
###

# Limpiar pantalla
import os
os.system("cls")

print("\nSentencia simple condicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")

edad = 15

# no entra en la condicion porque 15 no es mayor o igual a 18
if edad >= 18:
    print("Eres mayor de edad")

print("\nSentencia condicional con else")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\nSentencia condicional con elif")

edad = 18
if edad > 18:
    print("Tienes mas de 18 años")
elif edad < 18:
    print("Eres menor de edad")
else:
    print("Tienes 18 años justos")


# Operadores logicos
print("\nCondicional múltiples")

edad = 25
tiene_carnet = True

# operadores logicos en otros lenguajes
# and -> &&
# or  -> ||
# not -> !

if edad >= 18 and tiene_carnet:
    print("Puedes conducir un coche")
else:
    print("No puedes conducir un coche")

print("\n Anidar condiciones")

edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes salir de fiesta")
    else:
        print("No tienes dinero para salir de fiesta")
else:
    print("Eres menor de edad, no puedes salir de fiesta")

# Otra forma de hacerlo mas facil

if edad < 18:
    print("Eres menor de edad, no puedes salir de fiesta")
elif tiene_dinero:
    print("Puedes salir de fiesta")
else:
    print("No tienes dinero para salir de fiesta")

# 

numero = 5

if numero: # true si numero es distinto de cero
    print("El numero no es cero")

numero = 0

if numero: # false si numero es cero
    print("El numero no es cero")

nombre = "Juan"
if nombre: # true si la cadena no esta vacia
    print("El nombre no esta vacio")

nombre = ""
if nombre: # false si la cadena esta vacia
    print("El nombre no esta vacio")

numero = 5 # asignacion
if numero == 5: # comparacion
    print("El numero es 5")

print("\nLa condicion ternaria")

# es una forma concisa de un if-else en una linea de codigo
# [código si cumple la condicion] if [condición] else [código si no cumple la condición]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
