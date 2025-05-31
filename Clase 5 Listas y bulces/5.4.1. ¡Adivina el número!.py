'''
Clase:        #5
Tema:         Listas y bucles
Ejercicio:    5.4.1 ¡Adivina el número!
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.

Autor:        Keylen Celeste Méndez Sosa
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''
import random
n = random.randint(1, 100)

numero=""
while numero!=n:
    numero=int(input("Ingresa un numero entre 1 y 100: "))
    if numero==n:
        print(f"¡Felicidades! Has adivinado el número secreto: {numero}")
    elif numero<n:
        print("El número secreto es mayor")
    elif numero>n:
        print("El número secreto es menor")    