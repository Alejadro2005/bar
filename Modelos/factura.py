from Modelos.pedido import Pedido

class Factura:
    def __init__(self, pedido: Pedido, propina: float) -> None:
        self.pedido = pedido
        self.propina = propina

    def calcular_total(self) -> float:
        """Calcula el total de la factura (total del pedido + propina)."""
        return self.pedido.calcular_total() + self.propina

    def __str__(self) -> str:
        total_factura = self.calcular_total()
        return (f"Factura:\n{self.pedido}\n"
                f"Total: ${total_factura:.2f}\n"
                f"Propina: ${self.propina:.2f}\n")

    def to_dict(self) -> dict:
        """Convierte la factura en un diccionario para su almacenamiento en JSON."""
        return {
            'pedido': self.pedido.to_dict(),  # Asegúrate de que Pedido tenga un método to_dict()
            'propina': self.propina
        }
