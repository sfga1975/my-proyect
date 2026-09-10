"""Ejemplo sencillo de clientes, movimientos y cuentas bancarias."""

# Importamos random para generar un número aleatorio para cada cuenta.
import random


class Cliente:
    """Representa a una persona titular de una cuenta bancaria."""

    # Los atributos se escriben como privados para controlar su acceso.
    __dni: str
    __nombre: str
    __apellidos: str

    # El constructor recibe los datos necesarios para crear el cliente.
    def __init__(self, dni: str, nombre: str, apellidos: str):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    # Devuelve el nombre completo con los apellidos después.
    def get_nombre(self) -> str:
        return f"{self.__nombre}, {self.__apellidos}"

    # Permite consultar el DNI sin acceder directamente al atributo privado.
    def get_dni(self) -> str:
        return self.__dni

    # Devuelve únicamente el nombre del cliente.
    def get_nombre_propio(self) -> str:
        return self.__nombre

    # Devuelve únicamente los apellidos del cliente.
    def get_apellidos(self) -> str:
        return self.__apellidos


class Movimiento:
    """Representa un ingreso o una retirada de dinero."""

    # Un movimiento necesita un concepto y una cantidad.
    __concepto: str
    __cantidad: float

    def __init__(self, concepto: str, cantidad: float):
        self.__concepto = concepto
        self.__cantidad = cantidad

    # Devuelve la descripción del movimiento.
    def get_concepto(self) -> str:
        return self.__concepto

    # Devuelve la cantidad que se sumará al saldo.
    def get_cantidad(self) -> float:
        return self.__cantidad


class Cuenta:
    """Representa una cuenta bancaria asociada a un cliente."""

    # La cuenta guarda un número, un titular, un saldo y sus movimientos.
    __numero: str
    __titular: Cliente
    __saldo: float
    __movimientos: list[Movimiento]

    # El titular es obligatorio; el número y el saldo se generan aquí.
    def __init__(self, titular: Cliente):
        self.__titular = titular

        # randint incluye los dos extremos y produce exactamente 10 dígitos.
        self.__numero = str(random.randint(1_000_000_000, 9_999_999_999))
        self.__saldo = 0.0

        # Cada cuenta debe tener su propia lista de movimientos.
        self.__movimientos = []

    # Devuelve el número de cuenta.
    def get_numero(self) -> str:
        return self.__numero

    # Devuelve el cliente titular de la cuenta.
    def get_titular(self) -> Cliente:
        return self.__titular

    # Devuelve el saldo actual.
    def get_saldo(self) -> float:
        return self.__saldo

    # Devuelve la lista de movimientos registrados.
    def get_movimientos(self) -> list[Movimiento]:
        return self.__movimientos

    # Añade un movimiento y actualiza el saldo con su cantidad.
    def set_movimiento(self, movimiento: Movimiento) -> None:
        self.__movimientos.append(movimiento)
        self.__saldo += movimiento.get_cantidad()


# Este bloque solo se ejecuta cuando abrimos este archivo directamente.
if __name__ == "__main__":
    # Creamos una lista para guardar varios clientes.
    clientes: list[Cliente] = []

    # Añadimos dos clientes a la lista.
    clientes.append(Cliente("12345678Z", "Jose Antonio", "Ribera Ordoñez"))
    clientes.append(Cliente("87654321X", "Maria de la O", "Pérez Serrano"))

    # Recorremos la lista y mostramos los datos de cada cliente.
    for cliente in clientes:
        print(f"DNI: {cliente.get_dni()}, Nombre: {cliente.get_nombre()}")

    # Creamos una lista para guardar las cuentas bancarias.
    cuentas: list[Cuenta] = []

    # Creamos una cuenta cuyo titular es el primer cliente de la lista.
    cuentas.append(Cuenta(clientes[0]))
    cuenta_pepe = cuentas[0]
    print(
        f"Saldo inicial de {cuenta_pepe.get_titular().get_nombre()}: "
        f"{cuenta_pepe.get_saldo()} EUR"
    )

    # Registramos dos ingresos y una retirada.
    cuenta_pepe.set_movimiento(Movimiento("Ingreso inicial", 1000))
    cuenta_pepe.set_movimiento(Movimiento("Ingreso", 30))
    cuenta_pepe.set_movimiento(Movimiento("Retirada", -500))
    print(f"Saldo después de los movimientos: {cuenta_pepe.get_saldo()} EUR")

    # Buscamos las cuentas cuyo titular coincide con el primer cliente.
    dni_buscado = clientes[0].get_dni()
    for cuenta in cuentas:
        if cuenta.get_titular().get_dni() == dni_buscado:
            print(
                f"D. {cuenta.get_titular().get_nombre()} es titular de "
                f"la cuenta {cuenta.get_numero()} con un saldo de "
                f"{cuenta.get_saldo()} EUR"
            )
