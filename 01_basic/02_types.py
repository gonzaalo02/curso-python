###
# 02 - types()
# Python tiene varios tipos de datos
# int, float, complex,  str, bool, NoneType, list, tuple, dict, range, set ...
###

'''
    Asi puedes hacer una cadena de texto
    multilinea y si no lo asignas a nada...ç
    se trata como un comentario
'''

# tipos de datos basicos

# enteros
print("int:")
print(42)

print(type(42))  # muestra el tipo de dato
print(type(342846589732465879365287))  # en python los enteros son de precision ilimitada

# decimales
print("float:")
print(1.0) # aunquees .0 es un numero decimal, en python se representa como float
print(type(1.0))

# siempre que utilizas la notacion cientifica, estas trabajando con floats
print(1e3)  # 1 * 10^3
print(type(1e3))

# numeros complejos
print("complex:")
print(type(1 + 2j)) 

print("str:")
print(type("Hola"))
print(type("")) # una cadena vacia tambien es str
print(type("43")) # aunque parezca un numero, sigue siendo str ya que va con comillas

print("bool:")
print(type(True))
print(type(False))
print(type(1 > 2))  # las expresiones de comparacion devuelven bool

# el unico valor que representa la ausencia de valor en python es None
print("NoneType:")
print(type(None))

