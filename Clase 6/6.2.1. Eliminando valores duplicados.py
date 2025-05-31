'''
Clase:        #6
Tema:         Listas y bucles
Ejercicio:    6.2.1. Eliminando valores duplicados
Descripción:  Dada un a lista del usuario devuelve la misma lista eliminando los elementos duplicados

Autor:        Keylen Celeste Méndez Sosa
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numeros=input("Dame una lista de numeros (Ponme espacios entre números): ")
numeros=list(numeros.split(" "))
list_numero=[]

for num in numeros:
    if num not in list_numero:

        list_numero.append(num)    
list_numero = " ".join(list_numero)
print(list_numero)