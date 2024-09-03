from typing import Optional

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int, tipo: str, categoria: Optional[str] = '', tamaño: Optional[str] = '') -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.tipo = tipo
        self.categoria = categoria
        self.tamaño = tamaño

    def __str__(self) -> str:
        return f"{self.nombre} - ${self.precio} ({self.stock} en stock)"
