class Mesero:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.propinas_acumuladas = 0.0

    def agregar_propina(self, monto: float) -> None:
        self.propinas_acumuladas += monto

    def __str__(self) -> str:
        return f"{self.nombre} - Propinas: ${self.propinas_acumuladas:.2f}"
