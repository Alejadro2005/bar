from typing import Optional

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int, tipo: str, categoria: Optional[str] = '', tamaño: Optional[str] = '') -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.tipo = tipo
        self.categoria = categoria
        self.tamaño = tamaño

    def to_dict(self) -> dict:
        """Convierte el objeto Producto en un diccionario para la serialización a JSON."""
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "tipo": self.tipo,
            "categoria": self.categoria,
            "tamaño": self.tamaño
        }

    def __repr__(self) -> str:
        """Devuelve una representación en cadena del objeto Producto."""
        return (f"Producto(nombre={self.nombre}, precio={self.precio}, "
                f"stock={self.stock}, tipo={self.tipo}, "
                f"categoria={self.categoria}, tamaño={self.tamaño})")

    def __str__(self) -> str:
        """Devuelve una representación legible del producto."""
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"