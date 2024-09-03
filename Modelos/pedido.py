from typing import Dict
from Modelos.producto import Producto

class Pedido:
    def __init__(self, mesa_numero: int) -> None:
        self.mesa_numero = mesa_numero
        self.productos: Dict[Producto, int] = {}

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def __str__(self) -> str:
        productos_str = ', '.join([f"{producto.nombre} x{cantidad}" for producto, cantidad in self.productos.items()])
        return f"Mesa {self.mesa_numero}: {productos_str}"
