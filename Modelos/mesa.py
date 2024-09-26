class Mesa:
    def __init__(self, numero: int):
        self.numero = numero
        self.ocupada = False  # Atributo para saber si la mesa está ocupada

    def ocupar(self):
        """Marca la mesa como ocupada."""
        self.ocupada = True

    def liberar(self):
        """Marca la mesa como libre."""
        self.ocupada = False

    def __str__(self):
        """Devuelve una representación legible de la mesa."""
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Mesa {self.numero} - Estado: {estado}"
