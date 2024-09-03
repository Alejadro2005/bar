from Modelos.producto import Producto

class Plato(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, categoria: str) -> None:
        super().__init__(nombre, precio, stock, tipo='plato', categoria=categoria)
