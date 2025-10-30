###
# 04 - Functions
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

# Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2):
#   docstring opcional  
#   # Bloque de código
#   return valor_de_retorno_opcional

def saludar():
    print("Hola")

saludar()  # Llamada a la función

# Ejemplo de una funcion con parametro

def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Luis")

# Ejemplo de una función con retorno

def suma(a, b):
    suma = a + b
    return suma



resutado = suma(3, 5)
print(f"La suma es: {resutado}")


# Documentar las funciones

def restar(a, b):
    """Resta b de a y devuelve el resultado."""
    return a - b

print(restar.__doc__)  # Imprime la documentación de la función

# help(restar)

def multiplicar(a, b = 2):
    """Multiplica a por b y devuelve el resultado. b tiene un valor por defecto de 2."""
    return a * b

print(multiplicar(4))      # Usa el valor por defecto de b

# Argumentos por clave

def descripcion_persona(nombre, edad, sexo):
    print(f"Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}")

descripcion_persona(30,"gonzalo","masculino")  # Argumentos por posición
descripcion_persona(sexo="femenino", nombre="Maria", edad=25)  # Argumentos por clave

# Argumentos de longitud de variable.
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1,2,3,4,5))

###

sumar_numeros(10,20)
sumar_numeros(5,15,25,35,45,55)

# Argumentos de clave-valor variable (**kwargs):

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=28, ciudad="Madrid")
mostrar_info(profesion="Ingeniero", empresa="TechCorp")
mostrar_info(pais="Argentina", idioma="Español", moneda="Peso")

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

def tabla_multiplicar(a, b=10):
    for i in range(1, b + 1):
        print(f"{a} x {i} = {a * i}")

tabla_multiplicar(5)
