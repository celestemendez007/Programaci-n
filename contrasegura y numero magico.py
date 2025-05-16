'''
Clase:        #2
Tema:         Tema de la clase
Ejercicio:    Contraseña segura y numero magico
Descripción:  decir si una contraseña es segura cuando tiene por lo menos 1 numero y 1 letra mayuscula y si no que es no segura
              el otro es de que te dijera si un nimero era magico si era divisible entre 7 pero no entre 5

Autor:        Keylen Celeste Méndez Sosa
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
contra=input("Escribe una contraseña ")
hay_mayuscula=0
hay_letra=0
for letra in contra:
    if letra.isdigit():
        hay_letra=1
    if letra.isupper():
        hay_mayuscula=1
if hay_letra==1 and hay_mayuscula==1 and len(contra)>=8:
    print("Contra segura")
else:
    print("Contra no segura")

numero=int(input("Dame un numero "))
if numero%7==0 and numero%5!=0:
    print("Mágico")
else:
    print("No mágico")

