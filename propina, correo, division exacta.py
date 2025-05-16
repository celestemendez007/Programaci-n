'''
Clase:        #1
Tema:         Tema de la clase
Ejercicio:    propina, generador de correo y division exacta
Descripción:  La de propina era de evaluar segun el total de la cuenta un porcentaje para dar de propina y sumarla al total final
              La de generador de correo era de darle el nombre de estudiante y generara un correo electronico con @keyinstitute.edu.sv
              Y el ultimo era de dividir y que diera el numero de decimales de otro numero

Autor:        Keylen Celeste Méndez Sosa
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

#calculo de propina
total=int(input("Dame el total de tu cuenta "))
print("1. 10%\n","2. 15%\n","3. 20%")
numero=int(input("¿Cuanto quieres dar de propina:? (Pon solamente el numero)\n",))
if numero==1:
    diez=total*0.1
    print(f"Tu propina es ${diez} y en total pagaras ${diez+total}")
if numero ==2:
    quince=total*0.15
    print(f"Tu propina es ${quince} y en total pagaras ${quince+total}")
if numero ==3:
    veinte=total*0.2
    print(f"Tu propina es ${veinte} y en total pagaras ${veinte+total}")

#generador de correo
nombre=input("Dame tu nombre completo: ")
nombre=nombre.lower().split(" ")
print(f"{nombre[0]}.{nombre[2]}@keyinstitute.edu.sv")

#division con presicion
a,b,k=4,3,15
division=a/b
print(round(division, k))
