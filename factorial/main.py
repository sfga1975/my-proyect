def factorial(n: int) -> int | None:
    # Primero comprobamos el tipo para poder comparar n con cero sin errores.
    # type(n) is not int también rechaza valores como 3.0 y True.
    if type(n) is not int or n < 0:
        return None

    # El factorial de 0 y de 1 es 1.
    # Además, este valor sirve como resultado inicial de la multiplicación.
    resultado = 1

    # range no incluye el último valor, por eso usamos n + 1.
    # Por ejemplo, si n vale 5, i toma los valores 2, 3, 4 y 5.
    for i in range(2, n + 1):
        # Multiplicamos el resultado acumulado por el número actual.
        resultado *= i

    # Devolvemos el resultado final después de completar todas las iteraciones.
    return resultado


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    # Importamos la herramienta del ejercicio para leer los argumentos.
    import vendor

    # Ejecutamos factorial usando los valores definidos en args.py.
    vendor.launch(factorial)
