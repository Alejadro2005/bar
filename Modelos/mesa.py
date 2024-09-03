class Mesa:
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.ocupada = False

    def ocupar(self) -> None:
        self.ocupada = True

    def liberar(self) -> None:
        self.ocupada = False

    def __str__(self) -> str:
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Mesa {self.numero}: {estado}"
