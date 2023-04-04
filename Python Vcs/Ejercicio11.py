from functools import reduce

def x(lista):
    resultado = list(filter((lambda r: r % 2), lista))
    print(resultado)
    resultado = reduce((lambda r, y: r + y), resultado)
    print(resultado)

impar = list(range(1000))

x(impar)
