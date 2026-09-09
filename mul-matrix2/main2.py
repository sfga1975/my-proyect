def run(A: list, B: list) -> list:
    # Número de filas de la matriz A.
    filas = len(A)

    # Número de columnas de la matriz B.
    columnas = len(B[0])

    # Cantidad de elementos que se multiplicarán y sumarán.
    elementos = len(B)

    # Creamos la matriz resultado llena de ceros.
    # Tendrá tantas filas como A y tantas columnas como B.
    matriz_resultado = [[0] * columnas for _ in range(filas)]

    # Recorremos cada fila de la matriz A.
    for i in range(filas):

        # Recorremos cada columna de la matriz B.
        for j in range(columnas):

            # Recorremos los elementos necesarios para realizar
            # las multiplicaciones y sumarlas en la posición [i][j].
            for k in range(elementos):

                # Multiplicamos un elemento de A por uno de B
                # y acumulamos el resultado.
                matriz_resultado[i][j] += A[i][k] * B[k][j]

    # Devolvemos la matriz resultante.
    return matriz_resultado


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)