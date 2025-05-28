'''
Clase:        #2
Tema:         Tema de la clase
Ejercicio:    Contraseña segura, numero magico y calculo de impuesto
Descripción:  decir si una contraseña es segura cuando tiene por lo menos 1 numero y 1 letra mayuscula y si no que es no segura
              El de los impuestos es de que si las unidades consumidas son de oa a 100 no hay impuestos, si es de 101 a 200 se le aplica un $0.5 de impuestos y si es mas de 201 es de $0.7 
              el otro es de que te dijera si un nimero era magico si era divisible entre 7 pero no entre

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

consumo=int(input("Dame las unidades consumidas "))
if consumo<=100:
    print("Sin impuestos")
if consumo<=200 and consumo>=101:
    print(f"Tu impuesto es: {consumo*0.5}")
if consumo>=201:
    print(f"Tu impuesto es: {consumo*0.7}")

numero=int(input("Dame un numero "))
if numero%7==0 and numero%5!=0:
    print("Mágico")
else:
    print("No mágico")

