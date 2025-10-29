###
# 03 - casting de types
# transformar un tipo de valor a otro
###

# algunas de las transformaciones mas comunes

print("Conversión de tipos:")
print(type("100"))

# convertir str a int
print(type(int("100"))) # esto ahora es un entero
print(int("100") + 50)  # ahora podemos hacer operaciones matematicas

# convertir de int a str
print(type(str(100))) # esto ahora es una cadena de texto
print("100" + str(50))  # ahora podemos concatenar

# convertir str a float
print(type(float("12.34")))

# convertir float a int (pierde la parte decimal)
print(int(12.99))

# convertir int a bool (0 es False, cualquier otro numero es True)
print(bool(3)) # true  
print(bool(0)) # false
print(bool(-1)) # true

# convertir str a bool (cadenas vacias son False, cualquier otra es True)
print(bool("Hola")) # true
print(bool("")) # false
print(bool(" ")) # true (no es una cadena vacia, contiene un espacio)

# extra - round()
# redondear un numero decimal al entero mas cercano
print(round(3.14))  # 3
print(round(3.5))   # 4
print(round(2.5))   # 2  (redondea al numero par mas cercano)