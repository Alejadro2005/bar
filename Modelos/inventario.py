from typing import Dict, Optional
from Modelos.producto import Producto

class Inventario:
    def __init__(self) -> None:
        self.productos: Dict[str, Producto] = {}

    def agregar_producto(self, nombre: str, precio: float, stock: int, tipo: str, categoria: Optional[str] = '', tamaño: Optional[str] = '') -> None:
        producto = Producto(nombre, precio, stock, tipo, categoria, tamaño)
        self.productos[nombre] = producto

    def actualizar_stock(self, nombre: str, stock: int) -> None:
        if nombre in self.productos:
            self.productos[nombre].stock = stock

    def eliminar_producto(self, nombre: str) -> None:
        if nombre in self.productos:
            del self.productos[nombre]

    def verificar_disponibilidad(self, nombre: str, cantidad: int) -> bool:
        if nombre in self.productos:
            return self.productos[nombre].stock >= cantidad
        return False

    def mostrar_inventario(self) -> None:
        for producto in self.productos.values():
            print(producto)
