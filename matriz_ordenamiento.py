def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [7, 6, 1]
]

while True:
    try:
        fila_a_ordenar = int(input(f"Ingresar el número de la fila a ordenar, puede ser en el rango desde (0-{len(matriz)-1}): "))
        if 0 <= fila_a_ordenar < len(matriz):
            break
        else:
            print("Número de fila fuera del rango, intente de nuevo.")
    except ValueError:
        print("Por favor, ingrese un número.")

print("\nMatriz original:")
for fila in matriz:
    print(fila)

bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
