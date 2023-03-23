
# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

def imc (estatura, peso):

    "Calcula el Indice de la Masa Corporal."

    return peso / estatura ** 2

peso = float(input ('Introduce tu Peso en (Kg):'))
estatura = float (input ('Introduce Tu Altura en (m)'))

indice = imc (estatura, peso)

print ('Su Indice de Masa Corporal es: {}' .format(indice))