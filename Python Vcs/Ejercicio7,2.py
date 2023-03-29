from Ejercicio7 import JornadaTrabajo

def main():

    jornadatrabajo = JornadaTrabajo(0, 7)
    eshorariojornada = jornadatrabajo.eshorariojornada()
    if eshorariojornada == 0:
        print(
            f'Sigue trabajando!! te que dan {round(jornadatrabajo.finjornada()/3600,2)} horas para finalizar')
    else:
        print("Estas en tu tiempo libre, disfrutalo!")


if __name__ == "__main__":
    main()
