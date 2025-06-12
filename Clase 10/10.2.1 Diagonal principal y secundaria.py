N = int(input())
matriz = []
for x in range(N):
    fila = list(map(int, input().split(",")))
    matriz.append(fila)

diagonal_principal = []
diagonal_secundaria = []

for lista in range(N):
    for numero in range(N):
        if lista == numero:
            diagonal_principal.append(matriz[lista][numero])
        if lista + numero == N - 1:
            diagonal_secundaria.append(matriz[lista][numero])


print(diagonal_principal)
print(diagonal_secundaria)

