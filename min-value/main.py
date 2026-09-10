def run(values: list) -> int:
    # Comenzamos suponiendo que el primer valor es el menor.
    minimo = values[0]

    # Recorremos todos los valores de la lista.
    for valor in values:

        # Si encontramos un valor menor, actualizamos el mínimo.
        if valor < minimo:
            minimo = valor

    # Devolvemos el valor más pequeño.
    return minimo


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
