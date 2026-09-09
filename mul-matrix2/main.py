def run(A: list, B: list) -> list:
    # Creamos una matriz resultado de 2 filas y 2 columnas.
    Matriz2x2 = [[0, 0], [0, 0]]

    # Calculamos cada elemento de la matriz resultado.
    # Cada posición se obtiene multiplicando una fila de A
    # por una columna de B y sumando los dos productos.
    Matriz2x2[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    Matriz2x2[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    Matriz2x2[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    Matriz2x2[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    # Devolvemos la matriz con los cuatro resultados.
    return Matriz2x2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
