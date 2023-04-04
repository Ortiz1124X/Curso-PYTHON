from pickle import *

class Vehiculo:

    def __init__(self, color, puertas, motor, marca, modelo):
        self.color = color
        self.puertas = puertas
        self.motor = motor
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return self.color + " " + self.puertas + " " + self.motor + " " + self.marca + " " + self.modelo


lamborghini = Vehiculo("Azul", "4", "xtz", "Lamborghini", "Urus")
print(lamborghini)

f = open('vehiculo_objeto.txt', 'w+b')

dump(lamborghini, f)

f.seek(0)
nuevo_lamborghini = load(f)

print(nuevo_lamborghini)
f.close()