def run(xmin: int, xmax: int) -> list:
    # xmin es el primer número que vamos a utilizar.
    # xmax es el último número que vamos a utilizar.
    # range crea una sucesión desde xmin hasta xmax.
    # Sumamos 1 a xmax porque range no incluye su segundo límite.
    # La expresión 3 * x + 2 aplica la función a cada número de la sucesión.
    # La lista por comprensión reúne automáticamente todos los resultados.
    valores = [3 * x + 2 for x in range(xmin, xmax + 1)]

    # Devolvemos la lista completa de resultados.
    return valores


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
