from typing import Dict
from Modelos.producto import Producto

class Pedido:
    def __init__(self, mesa_numero: int) -> None:
        self.mesa_numero = mesa_numero
        self.productos: Dict[Producto, int] = {}  # Mapeo de productos a cantidades

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        """Agrega un producto al pedido con la cantidad especificada."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        # Verifica si el producto ya está en el pedido
        if producto in self.productos:
            self.productos[producto] += cantidad  # Suma la cantidad si ya existe
        else:
            self.productos[producto] = cantidad  # Agrega el nuevo producto

    def calcular_total(self) -> float:
        """Calcula el total del pedido sumando el precio de todos los productos."""
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos.items())
        return total

    def to_dict(self) -> dict:
        """Convierte el pedido a un diccionario para serialización."""
        return {
            "mesa_numero": self.mesa_numero,
            "productos": {producto.nombre: cantidad for producto, cantidad in self.productos.items()}
        }

    def __str__(self) -> str:
        """Devuelve una representación en cadena del pedido."""
        if not self.productos:
            return f"Mesa {self.mesa_numero}: Sin productos"
        productos_str = ', '.join([f"{producto.nombre} x{cantidad}" for producto, cantidad in self.productos.items()])
        return f"Mesa {self.mesa_numero}: {productos_str}"
