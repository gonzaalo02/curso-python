"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""


import os
os.system("cls")

text = "RRRRJJJjjjrrr"

def comprobar_equilibrio(text):
    text = text.upper()
    count_R = text.count('R')
    count_J = text.count('J')

    print(f"Cantidad de R: {count_R} | Cantidad de J: {count_J}")
    
    # if count_R == count_J:
    #     return True
    # else:
    #     return False

    return count_R == count_J
    

print(comprobar_equilibrio("RRjJ"))


