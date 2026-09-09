import sys

# Mostramos todos los elementos recibidos en la línea de comandos.
# El primer elemento es el nombre o la ruta del archivo ejecutado.
for elemento in sys.argv:
	print(elemento)

suma: int = sum([int(numero) for numero in sys.argv[1:]])
longitud: int = len(sys.argv[1:])

# :.2f redondea el resultado y muestra siempre dos decimales.
media = f"{suma / longitud:.2f}"

print(media)