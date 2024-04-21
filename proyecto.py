from random import randint
from time import sleep

nombre = str(input("¡Hola! ¿Cómo te llamas? ")).capitalize()
print("¡Bienvenid@!",nombre)

aleatorio = randint(1,100)
print("Bueno, he pensado un número entre 1 y 100, y tienes solo diez intentos para adivinar cuál crees que es este número.")
intentos = 0
while intentos < 11:
    for i in range(1,11):
        intentos += 1
        numero = int(input(f"{i}º Intento: "))
        print("Comparando los números...\n")
        sleep(0.6)
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
    break
if intentos == 10:
    print("Lo siento, se han agotado tus intentos.")
