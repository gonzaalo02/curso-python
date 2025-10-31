
class Coche:
    tipo = "vehiculo de cuatro ruedas" # Este atributo es común a todos los coches

    def __init__(self, marca, modelo, color): # este es el constructor que se ejecuta al crear un objeto
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        return f"El coche {self.marca} {self.modelo} ha arrancado."
    

coche_1 = Coche("Toyota", "Corolla", "Rojo")
coche_2 = Coche("Honda", "Civic", "Azul")

print(coche_1.arrancar())  # Llama al método arrancar del objeto coche_1
print(coche_2.arrancar())  # Llama al método arrancar del objeto coche_2