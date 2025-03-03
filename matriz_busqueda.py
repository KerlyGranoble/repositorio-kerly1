def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz."

matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [7, 6, 1]
]

valor_a_buscar = int(input("Ingrese el valor que desea buscar: "))
print(buscar_valor(matriz, valor_a_buscar))
