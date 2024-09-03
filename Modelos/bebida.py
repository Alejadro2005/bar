from Modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, tamaño: str) -> None:
        super().__init__(nombre, precio, stock, tipo='bebida', tamaño=tamaño)
