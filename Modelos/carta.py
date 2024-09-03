from typing import List
from Modelos.producto import Producto

class Carta:
    def __init__(self) -> None:
        self.productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def mostrar_carta(self) -> None:
        for producto in self.productos:
            print(producto)
