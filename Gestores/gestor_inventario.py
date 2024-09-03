import json
from Modelos.inventario import Inventario
from Modelos.producto import Producto

class GestorInventario:
    def __init__(self) -> None:
        self.inventario = Inventario()

    def agregar_producto(self, nombre: str, precio: float, stock: int, tipo: str, categoria: str = '', tamaño: str = '') -> None:
        if tipo == 'plato':
            self.inventario.agregar_producto(nombre, precio, stock, tipo, categoria)
        elif tipo == 'bebida':
            self.inventario.agregar_producto(nombre, precio, stock, tipo, tamaño=tamaño)

    def actualizar_stock(self, nombre: str, stock: int) -> None:
        self.inventario.actualizar_stock(nombre, stock)

    def eliminar_producto(self, nombre: str) -> None:
        self.inventario.eliminar_producto(nombre)

    def verificar_disponibilidad(self, nombre: str, cantidad: int) -> bool:
        return self.inventario.verificar_disponibilidad(nombre, cantidad)

    def mostrar_inventario(self) -> None:
        self.inventario.mostrar_inventario()

    def cargar_inventario_desde_json(self, archivo_json: str) -> None:
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
            for producto in datos:
                nombre = producto['nombre']
                precio = producto['precio']
                stock = producto['stock']
                tipo = producto['tipo']
                categoria = producto.get('categoria', '')
                tamaño = producto.get('tamaño', '')
                self.agregar_producto(nombre, precio, stock, tipo, categoria, tamaño)
