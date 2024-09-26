import json
from typing import Optional
from Modelos.producto import Producto  # Asegúrate de que esta línea esté presente


class Inventario:
    def __init__(self) -> None:
        self.productos = []

    def agregar_producto(self, nombre: str, precio: float, stock: int, tipo: str,
                         categoria: Optional[str] = '', tamaño: Optional[str] = '') -> None:
        # Verifica si el producto ya existe en el inventario
        for producto in self.productos:
            if producto.nombre == nombre:
                # Si el producto ya existe, incrementa su stock
                producto.stock += stock
                return

        # Si no existe, crea un nuevo producto y agrégalo
        producto = Producto(nombre, precio, stock, tipo, categoria, tamaño)
        self.productos.append(producto)

    def obtener_producto(self, nombre: str) -> Optional[Producto]:
        # Busca y devuelve el producto por nombre
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None  # Retorna None si no se encuentra el producto

    def actualizar_stock(self, nombre: str, nuevo_stock: int) -> None:
        producto = self.obtener_producto(nombre)
        if producto:
            producto.stock = nuevo_stock
        else:
            raise ValueError(f"Producto {nombre} no encontrado en el inventario.")

    def eliminar_producto(self, nombre: str) -> None:
        producto = self.obtener_producto(nombre)
        if producto:
            self.productos.remove(producto)
        else:
            raise ValueError(f"Producto {nombre} no encontrado en el inventario.")

    def verificar_disponibilidad(self, nombre: str, cantidad: int) -> bool:
        producto = self.obtener_producto(nombre)
        return producto is not None and producto.stock >= cantidad

    def mostrar_inventario(self) -> None:
        print("--- Inventario ---")
        if not self.productos:
            print("El inventario está vacío.")
            return

        for i, producto in enumerate(self.productos, start=1):
            print(f"{i}. Nombre: {producto.nombre}, Precio: ${producto.precio:.2f}, Stock: {producto.stock}, Tipo: {producto.tipo}, Categoría: {producto.categoria}, Tamaño: {producto.tamaño}")

    def cargar_inventario_desde_json(self, archivo_json: str) -> None:
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
            for item in datos:
                self.agregar_producto(
                    nombre=item['nombre'],
                    precio=item['precio'],
                    stock=item['stock'],
                    tipo=item['tipo'],
                    categoria=item.get('categoria', ''),
                    tamaño=item.get('tamaño', '')
                )

    def sobreescribir_inventario_json(self, archivo_json: str) -> None:
        datos_inventario = []
        for producto in self.productos:
            datos_inventario.append({
                'nombre': producto.nombre,
                'precio': producto.precio,
                'stock': producto.stock,
                'tipo': producto.tipo,
                'categoria': producto.categoria,
                'tamaño': producto.tamaño
            })

        with open(archivo_json, 'w') as file:
            json.dump(datos_inventario, file, indent=4)
