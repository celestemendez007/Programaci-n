fila = int(input())
columna = int(input())

matriz = []
for lista in range(fila):
    filas= list(map(int, input().split(",")))
    if len(filas) != columna:
        print("No es el largo de columna")
        exit()
    matriz.append(filas)

direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1),(0, 1),(1, -1),  (1, 0), (1, 1)]
lista_unos=[]
for lista in range(fila):
    lista_fila_unos = []
    for numeros in range(columna):
        unos = 0
        for x,y in direcciones:
            lista_comparar = lista + x
            numeros_comparar = numeros + y
            if 0 <= lista_comparar < fila and 0 <= numeros_comparar < columna:
                if matriz[lista_comparar][numeros_comparar] == 1:
                    unos += 1

        lista_fila_unos.append(unos)
    lista_unos.append(lista_fila_unos)

for fila_resultado in lista_unos:
    print(fila_resultado)
