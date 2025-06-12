N = int(input())
matriz = []
for x in range(N):
    fila = list(map(int, input().split(",")))
    matriz.append(fila)

contador=0
for lista in range(N):
    for numero in range(N):
        if matriz[lista][numero] != matriz[numero][lista]:
            contador=1
            

if contador==1:
    print("La matriz no es simetrica")
else:
    print("La matriz es simetrica")