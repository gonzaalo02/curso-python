###
# 04 - Variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinámico y de tipado fuerte
###

# Asignar una varable
# solo hace falta poner esto:
my_name = "Gonzalo"

# Imprimir la variable
print(my_name)

age = 32
print(age)

# Puedo cambiar el valor de la variable
age = 39
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución
# que no tienes que declararlo expliocitamente

name = "Gonzalo"
print(type(name))

name = 32
print(type(name))

#  Tipado fuerte: Python no realiza conversiones de tipo automáticas
print(10 + "2")

# f-strings (literal de cadena formato)
# desde la version 3.6 de Python
print(f"Mi nombre es {my_name} y tengo {age - 20} años.")

# No recomendada forma de asignar variables
name, age, city = "Gonzalo", 32, "Madrid"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok"      # snake_case (recomendado en Python)

MiNombreDeVariable = "ko"       # pascalCase (no recomendado en Python)
minombredevariable = "ko"       # todojunto (no recomendado)

mi_nombre_de_variable_123 = "ok"  # se pueden usar números, pero no al inicio

MI_CONSTANTE = 3.14          # no hay constantes reales, pero se usan mayúsculas para indicarlas

# Error declaracion de varuiables
# 12nombre = "Gonzalo"  # no puede empezar por número
# mi-nombre = "Gonzalo"  # no puede tener guiones
# mi nombre = "Gonzalo"  # no puede tener espacios
# def = "Gonzalo"        # no puede usar palabras reservadas

is_user_logged_in: bool = True  # anotación de tipo (opcional)
print(is_user_logged_in)

is_user_logged_in = 43
print(is_user_logged_in) # Python no impide cambiar el tipo de dato