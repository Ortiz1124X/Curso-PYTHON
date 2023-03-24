
class Vehiculo:

    color = "Negro"
    ruedas = "4 Ruedas"
    puertas = "5 Puertas"

class Coche(Vehiculo):

    velocidad = "120 km/h"
    cilindraje = "3996 cc"
    vehiculo = Vehiculo()

c = Coche
print("La Velocidad de la Lamborghini Urus es de:", c.velocidad)
print("El Clinidraje de nuestra Urus es de:", c.cilindraje)
print("Es de Color:", c.color)
print ("Su cantidad de Puertas es:", c.puertas)
print("Su cantidad de:", c.ruedas)





