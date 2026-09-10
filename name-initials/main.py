def run(fullname: str) -> str:
    # Dividimos el texto en dos partes usando ", " como separador:
    # [0] contiene los apellidos y [1] contiene el nombre.
    # Ejemplo: "Delgado Quintero, sergio"
    # Resultado: ["Delgado Quintero", "sergio"]
    apellidos_nombre: list[str] = fullname.split(sep=", ")

    # Separamos los apellidos por espacios para obtener una lista.
    # Ejemplo: ["Delgado", "Quintero"]
    apellidos: list[str] = apellidos_nombre[0].split()

    # Tomamos la primera letra del nombre, la convertimos a mayúscula
    # y añadimos un punto.
    # Ejemplo: "sergio" -> "S."
    inicial_nombre: str = apellidos_nombre[1][0].upper() + "."

    # Obtenemos la inicial del primer apellido y añadimos un punto.
    inicial_apellidos: str = apellidos[0][0].upper() + "."

    # Si existe un segundo apellido, obtenemos también su inicial.
    if len(apellidos) > 1:
        inicial_apellidos += apellidos[1][0].upper() + "."

    # Unimos la inicial del nombre con las iniciales de los apellidos.
    # Ejemplo: "S." + "D.Q." -> "S.D.Q."
    return inicial_nombre + inicial_apellidos


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)