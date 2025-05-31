'''
Clase:        #6
Tema:         Listas y bucles
Ejercicio:    6.3.1. Numeros lideres
Descripción:  Imprime el numero que es mayor al numero de la derecha 

Autor:        Keylen Celeste Méndez Sosa
Fecha:        2025-05-30
Estado:       [ En proceso ]
'''

numeros=input("Dame una lista de numeros (Ponme espacios entre números): ")
numeros=list(numeros.split(" "))
list_numero=[]
contador=1

for num in numeros:
    num=int(num)
    comparacion=int(numeros[contador])
    if num>comparacion:
        print(num, end=" ") 
    contador+=1 
    if contador==len(numeros):
        break




