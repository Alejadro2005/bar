from Modelos.pedido import Pedido

class Factura:
    def __init__(self, pedido: Pedido, propina: float) -> None:
        self.pedido = pedido
        self.propina = propina

    def calcular_total(self) -> float:
        total = sum(producto.precio * cantidad for producto, cantidad in self.pedido.productos.items())
        return total + self.propina

    def __str__(self) -> str:
        return f"{self.pedido}\nPropina: ${self.propina:.2f}\nTotal: ${self.calcular_total():.2f}"
