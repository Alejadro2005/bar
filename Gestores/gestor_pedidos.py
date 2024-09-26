import json
from typing import Dict, List
from Modelos.pedido import Pedido
from Modelos.factura import Factura
from Gestores.gestor_inventario import GestorInventario
from Gestores.gestor_mesas import GestorMesas


class GestorPedidos:
    def __init__(self, gestor_inventario: GestorInventario, gestor_mesas: GestorMesas) -> None:
        self.gestor_inventario = gestor_inventario
        self.gestor_mesas = gestor_mesas
        self.pedidos: Dict[int, List[Pedido]] = {}
        self.cargar_pedidos_desde_json('data/pedidos.json')

    def crear_pedido(self, mesa_numero: int, productos: Dict[str, int]) -> None:
        mesa = self.gestor_mesas.obtener_mesa(mesa_numero)
        if mesa is None:
            raise ValueError(f"La mesa {mesa_numero} no existe.")

        if mesa_numero not in self.pedidos:
            self.pedidos[mesa_numero] = []

        nuevo_pedido = Pedido(mesa_numero)
        for nombre, cantidad in productos.items():
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que 0.")

            if not self.gestor_inventario.verificar_disponibilidad(nombre, cantidad):
                raise ValueError(f"El producto {nombre} no está disponible.")

            producto = next((p for p in self.gestor_inventario.inventario.productos if p.nombre == nombre), None)
            if producto is None:
                raise ValueError(f"El producto {nombre} no se encontró en el inventario.")

            nuevo_pedido.agregar_producto(producto, cantidad)
            self.gestor_inventario.actualizar_stock(nombre, producto.stock - cantidad)

        self.pedidos[mesa_numero].append(nuevo_pedido)

        # Notificar a GestorMesas para marcar la mesa como ocupada
        self.gestor_mesas.marcar_mesa_ocupada(mesa_numero)

        self.guardar_pedidos_en_json('data/pedidos.json')

    def entregar_pedido(self, mesa_numero: int, propina: float) -> None:
        if mesa_numero not in self.pedidos or not self.pedidos[mesa_numero]:
            raise ValueError(f"No hay pedidos registrados para la mesa {mesa_numero}.")

        pedidos_entregados = self.pedidos.pop(mesa_numero)  # Eliminar todos los pedidos de la mesa
        factura = self.generar_factura(pedidos_entregados, propina)
        print(f"Factura generada:\n{factura}")

        # Notificar a GestorMesas para marcar la mesa como libre
        self.gestor_mesas.marcar_mesa_libre(mesa_numero)

        self.guardar_pedidos_en_json('data/pedidos.json')
        print(f"Todos los pedidos de la mesa {mesa_numero} fueron entregados y la mesa está libre.")

    def cargar_pedidos_desde_json(self, archivo_json: str) -> None:
        try:
            with open(archivo_json, 'r') as file:
                datos = json.load(file)
                for pedido_data in datos:
                    mesa_numero = pedido_data['mesa']
                    productos = pedido_data['productos']

                    mesa = self.gestor_mesas.obtener_mesa(mesa_numero)
                    if mesa is None:
                        print(f"La mesa {mesa_numero} no existe. Saltando este pedido.")
                        continue

                    if mesa_numero not in self.pedidos:
                        self.pedidos[mesa_numero] = []

                    nuevo_pedido = Pedido(mesa_numero)
                    for nombre, cantidad in productos.items():
                        producto = next((p for p in self.gestor_inventario.inventario.productos if p.nombre == nombre),
                                        None)
                        if producto:
                            nuevo_pedido.agregar_producto(producto, cantidad)
                    self.pedidos[mesa_numero].append(nuevo_pedido)

                    # Notificar a GestorMesas para marcar la mesa como ocupada
                    self.gestor_mesas.marcar_mesa_ocupada(mesa_numero)

        except FileNotFoundError:
            print("Archivo de pedidos no encontrado. Se iniciará con pedidos vacíos.")
        except json.JSONDecodeError:
            print("Error al leer el archivo de pedidos. Se iniciará con pedidos vacíos.")

    def generar_factura(self, pedidos_entregados: List[Pedido], propina: float) -> Factura:
        mesa_numero = pedidos_entregados[0].mesa_numero  # Obtener el número de mesa de uno de los pedidos
        total_pedido = Pedido(mesa_numero=mesa_numero)

        for pedido in pedidos_entregados:
            for producto, cantidad in pedido.productos.items():
                total_pedido.agregar_producto(producto, cantidad)  # Agrega el producto con su cantidad

        factura = Factura(total_pedido, propina)
        return factura

    def guardar_pedidos_en_json(self, archivo_json: str) -> None:
        pedidos_a_guardar = [
            {
                "mesa": mesa_numero,
                "productos": {producto.nombre: cantidad for producto, cantidad in pedido.productos.items()}
            }
            for mesa_numero, lista_pedidos in self.pedidos.items() for pedido in lista_pedidos
        ]
        with open(archivo_json, 'w') as file:
            json.dump(pedidos_a_guardar, file, indent=4)  # Guarda con formato bonito
