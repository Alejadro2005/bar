import json
from typing import Dict
from Modelos.inventario import Inventario
from Modelos.producto import Producto


class GestorInventario:
    def __init__(self) -> None:
        self.inventario = Inventario()
        self.cargar_inventario_desde_json('data/inventario.json')

    def agregar_producto(self, nombre: str, precio: float, stock: int, tipo: str, categoria: str = '',
                         tamaño: str = '') -> None:
        """Agrega un nuevo producto al inventario si no existe."""
        if not nombre or precio < 0 or stock < 0:
            raise ValueError("Nombre, precio y stock deben ser válidos.")

        if self.obtener_producto(nombre):
            print(f"El producto {nombre} ya existe en el inventario.")
            return  # No hace nada si el producto ya existe

        self.inventario.agregar_producto(nombre, precio, stock, tipo, categoria, tamaño)
        self.sobrescribir_inventario_json()

    def actualizar_stock(self, nombre: str, nuevo_stock: int) -> None:
        if nuevo_stock < 0:
            raise ValueError("El nuevo stock no puede ser negativo.")

        producto = self.obtener_producto(nombre)
        if producto:
            producto.stock = nuevo_stock
            self.sobrescribir_inventario_json()
        else:
            raise ValueError(f"Producto {nombre} no encontrado en el inventario.")

    def eliminar_producto(self, nombre: str) -> None:
        """Elimina un producto del inventario por su nombre."""
        producto = self.obtener_producto(nombre)
        if producto:
            self.inventario.eliminar_producto(nombre)
            self.sobrescribir_inventario_json()
        else:
            raise ValueError(f"Producto {nombre} no encontrado en el inventario.")

    def verificar_disponibilidad(self, nombre: str, cantidad: int) -> bool:
        """Verifica si hay suficiente stock de un producto."""
        if cantidad < 0:
            raise ValueError("La cantidad a verificar no puede ser negativa.")

        producto = self.obtener_producto(nombre)
        if producto:
            return producto.stock >= cantidad
        else:
            print(f"Producto {nombre} no encontrado.")
            return False

    def mostrar_inventario(self) -> None:
        """Muestra todos los productos del inventario."""
        if not self.inventario.productos:
            print("No hay productos en el inventario.")
            return
        self.inventario.mostrar_inventario()

    def cargar_inventario_desde_json(self, archivo_json: str) -> None:
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(archivo_json, 'r') as f:
                data = json.load(f)
                for item in data:
                    if not self.obtener_producto(item['nombre']):
                        self.agregar_producto(
                            item['nombre'], item['precio'], item['stock'],
                            item['tipo'], item.get('categoria', ''), item.get('tamaño', '')
                        )
        except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
            print(f"Error cargando el archivo JSON: {e}")

    def sobrescribir_inventario_json(self) -> None:
        """Sobrescribe el inventario en el archivo JSON solo si hay cambios."""
        with open('data/inventario.json', 'w') as file:
            json.dump([producto.to_dict() for producto in self.inventario.productos], file, indent=4)

    def obtener_producto(self, nombre: str):
        """Obtiene un producto del inventario por su nombre."""
        return next((producto for producto in self.inventario.productos if producto.nombre == nombre), None)

    def obtener_stock(self, nombre: str) -> int:
        """Retorna el stock actual de un producto."""
        producto = self.obtener_producto(nombre)
        if producto:
            return producto.stock
        else:
            raise ValueError(f"Producto {nombre} no encontrado en el inventario.")

    def mostrar_productos_disponibles(self) -> Dict[str, Producto]:
        productos = self.inventario.productos  # Acceder directamente al inventario
        print("\n--- Productos Disponibles ---")
        for producto in productos:
            print(f"{producto.nombre}: ${producto.precio} ({producto.stock} en stock)")
        return {producto.nombre: producto for producto in productos}
