nombre = str(input("¡Hola! ¿Cómo te llamas? ")).capitalize()
print("¡Bienvenid@!",nombre)

from random import randint
from time import sleep

aleatorio = randint(1,100)
print("Bueno, he pensado un número entre 1 y 100, y tienes solo diez intentos para adivinar cuál crees que es este número")
intentos = 0
while intentos < 11:
    for i in range(1,11):
        numero = int(input(f"{i}º Intento: "))
        print("Comparando los números...\n")
        sleep(1)
        if numero < 1 or numero > 100:
            print("Has elegido un número que no está permitido.")
        elif numero < aleatorio:
            print("Respuesta Incorrecta :( El número indicado es menor al número sorteado.")
        elif numero > aleatorio:
            print("Respuesta Incorrecta :( El número indicado es mayor al número sorteado.")
        elif numero == aleatorio:
            print("Respuesta correcta. ¡ENHORABUENA!")
            print(f"Has logrado con {intentos} intentos.")
            break
        intentos += 1
    break
