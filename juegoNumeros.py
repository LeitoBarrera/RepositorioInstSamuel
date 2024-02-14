import random

def adivinanza():
    numero_s = random.randint(1, 10)
    intentos_max = 5

    for intento_actual in range(1, intentos_max + 1):
        try:
            numero_u = int(input("Ingresa un número entre 1 y 10: "))
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue

        if numero_u == numero_s:
            print("¡Muy bien! Has acertado el número. ¡FELICITACIONES!")
            break
        elif numero_u < 1 or numero_u > 10:
            print("Error: Ingresa un número válido entre 1 y 10.")
        elif numero_u > numero_s:
            print("El número ingresado es mayor a el numero secreto, intente de nuevo.")
        else:
            print("El número ingresado es menor a el numero secreto. Intente de nuevo.")

    else:
        print(f"Lo siento, has agotado tus {intentos_max} intentos. El número era {numero_s}.")

adivinanza()
