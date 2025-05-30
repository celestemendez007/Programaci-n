numeros=input("Dame una lista de numeros (Ponme espacios entre números): ")
numeros=list(numeros.split(" "))
list_numero=[]

for num in numeros:
    if num not in list_numero:

        list_numero.append(num)    
list_numero = " ".join(list_numero)
print(list_numero)