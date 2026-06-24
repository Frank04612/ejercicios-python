import random

numero = random.randint(1, 100)
print("!Bienvenido al juego de adivinar el número!")
while True:
    intento = int(input("Ingrese un número entre 1 y 100: "))
    if intento < numero:
        print("Demasiado bajo, intenta de nuevo.")
    elif intento > numero:
        print("Demasiado alto, intenta de nuevo.")
    else:
        print("!Felicidades! Has adivinado el número.")