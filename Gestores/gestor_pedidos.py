import json
from typing import Dict
from Modelos.pedido import Pedido
from Gestores.gestor_inventario import GestorInventario
from Gestores.gestor_mesas import GestorMesas

class GestorPedidos:
    def __init__(self, gestor_inventario: GestorInventario, gestor_mesas: GestorMesas) -> None:
        self.gestor_inventario = gestor_inventario
        self.gestor_mesas = gestor_mesas
        self.pedidos: Dict[int, Pedido] = {}

    def crear_pedido(self, mesa_numero: int, productos: Dict[str, int]) -> None:
        mesa = self.gestor_mesas.obtener_mesa(mesa_numero)
        if mesa and mesa.ocupada:
            pedido = Pedido(mesa_numero)
            for nombre, cantidad in productos.items():
                if self.gestor_inventario.verificar_disponibilidad(nombre, cantidad):
                    producto = self.gestor_inventario.inventario.productos[nombre]
                    pedido.agregar_producto(producto, cantidad)
                    self.gestor_inventario.actualizar_stock(nombre, producto.stock - cantidad)
                else:
                    raise ValueError(f"El producto {nombre} no está disponible.")
            self.pedidos[mesa_numero] = pedido
        else:
            raise ValueError(f"La mesa {mesa_numero} no está ocupada o no existe.")

    def cargar_pedidos_desde_json(self, archivo_json: str) -> None:
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
            for pedido_data in datos:
                mesa_numero = pedido_data['mesa']
                productos = pedido_data['productos']
                self.gestor_mesas.marcar_mesa_ocupada(mesa_numero)  # Marcar la mesa como ocupada
                self.crear_pedido(mesa_numero, productos)
