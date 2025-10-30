"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

import os
os.system("cls")

def count_eggs(eggs_list) -> int:
    """Esta funcion recibe una lista de numeros enteros que representan la cantidad de huevos que han puesto diferentes dinosaurios en el parque jurásico y los numeros par son de carnivoros. Devuelve un numero con la suma de todos los huevos de carnivoros
    """
    total_eggs = 0
    for eggs in eggs_list:
        if eggs % 2 == 0:
            total_eggs += eggs
    
    return total_eggs

egg_list = [3, 4, 7, 5, 8]
print(count_eggs(egg_list))



