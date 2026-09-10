# TODO
class MobilePhone:
    # Estos son valores iniciales y anotaciones de los datos del teléfono.
    # Cada objeto recibe sus valores concretos en __init__.
    manufacturer: str = ""
    screen_size: float = 0.0
    num_cores: int = 0
    apps: list[str]
    status: bool = False

    # __init__ se ejecuta automáticamente al crear un MobilePhone.
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        # Guardamos en el objeto los datos recibidos como argumentos.
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores

        # La lista debe crearse aquí para que cada teléfono tenga sus propias apps.
        self.apps = []
        
        self.status = False

    # Encender el teléfono significa cambiar status a True.
    def power_on(self):
        self.status = True

    # Apagar el teléfono significa cambiar status a False.
    def power_off(self):
        self.status = False

    # El asterisco permite recibir una o varias aplicaciones.
    # Ejemplos: install_app("Twitter") o install_app("Twitter", "WhatsApp").
    def install_app(self, *app_names: str):
        # Recorremos todos los nombres recibidos.
        for app_name in app_names:
            # Solo añadimos la app si todavía no está instalada.
            if app_name not in self.apps:
                self.apps.append(app_name)

    # También podemos recibir una o varias aplicaciones para desinstalarlas.
    def uninstall_app(self, *app_names: str):
        # Recorremos todos los nombres recibidos.
        for app_name in app_names:
            # remove elimina la app únicamente si existe en la lista.
            if app_name in self.apps:
                self.apps.remove(app_name)
