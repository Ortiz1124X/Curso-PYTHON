
contador1 = 1

while contador1 <= 10:
    contador1 += 1

    if contador1 % 2 == 0:
        print(contador1, "Es un nummero par")
        continue

    print("Estoy aqui, por que el contador vale", contador1, "Y no se ha disparado el continue")

print("Fuera del While")