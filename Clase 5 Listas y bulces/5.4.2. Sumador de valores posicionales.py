'''
Clase:        #5
Tema:         Listas y bucles
Ejercicio:    5.4.2. Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

Autor:        Keylen Celeste Méndez Sosa
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''


numero=input("Ingresa un numero:")

print(f"Proceso de reducción para {numero}:")
lista_num=[]

while True:
    for num in numero:
        lista_num.append(int(num))
    lista_num=sum(lista_num)
    print(f"{numero}={lista_num}")
    if lista_num < 10:
        break
    numero=str(lista_num)
    lista_num=[]

print(f"El resultado final es {lista_num}")

    


