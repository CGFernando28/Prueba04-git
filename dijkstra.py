import random

def jugar_adivina_numero():
    print("¡Bienvenido al juego de adivinanza de números!")
    numero_secreto = random.randint(1, 100)  # Genera un número entre 1 y 100
    intentos = 0
    max_intentos = 10

    while intentos < max_intentos:
        try:
            suposicion = int(input("Adivina un número entre 1 y 100: "))
            intentos += 1

            if suposicion < 1 or suposicion > 100:
                print("Por favor, elige un número entre 1 y 100.")
                continue

            if suposicion < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif suposicion > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    if intentos == max_intentos:
        print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.")

if __name__ == "__main__":
    jugar_adivina_numero()
