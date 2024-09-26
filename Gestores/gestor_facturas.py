from typing import List, Optional
from Modelos.factura import Factura
from Gestores.gestor_inventario import GestorInventario
import json
from Modelos.pedido import Pedido


class GestorFacturas:
    def __init__(self) -> None:
        self.facturas: List[Factura] = []

    def agregar_factura(self, factura: Factura) -> None:
        if not isinstance(factura, Factura):
            raise ValueError("El objeto proporcionado no es una factura válida.")
        self.facturas.append(factura)

    def mostrar_facturas(self) -> None:
        if not self.facturas:
            print("No hay facturas registradas.")
            return
        for factura in self.facturas:
            print(factura)

    def buscar_factura(self, mesa_numero: int) -> Optional[Factura]:
        if mesa_numero <= 0:
            raise ValueError("El número de mesa debe ser mayor que cero.")
        for factura in self.facturas:
            if factura.pedido.mesa_numero == mesa_numero:
                return factura
        return None

    def calcular_total_factura(self, factura: Factura, gestor_inventario: GestorInventario) -> float:
        if factura not in self.facturas:
            raise ValueError("La factura no está registrada.")
        total = 0
        for producto_nombre, cantidad in factura.pedido.productos.items():
            producto = gestor_inventario.obtener_producto(producto_nombre)
            if producto:
                total += producto.precio * cantidad
            else:
                print(f"Producto {producto_nombre} no encontrado en el inventario.")
        return total + factura.propina


    def guardar_facturas_a_json(self, archivo_json: str) -> None:
        try:
            with open(archivo_json, 'w') as file:
                json.dump([factura.to_dict() for factura in self.facturas], file, indent=4)
        except Exception as e:
            print(f"Ocurrió un error al guardar las facturas en {archivo_json}: {e}")

    def cargar_facturas_de_json(self, archivo_json: str, gestor_inventario: GestorInventario) -> None:
        try:
            with open(archivo_json, 'r') as file:
                datos = json.load(file)
                for factura_data in datos:
                    pedido_data = factura_data['pedido']
                    pedido = self._crear_pedido_desde_datos(pedido_data, gestor_inventario)
                    factura = Factura(pedido, factura_data['propina'])
                    self.agregar_factura(factura)
        except FileNotFoundError:
            print(f"Archivo {archivo_json} no encontrado. No se cargaron facturas.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON {archivo_json}.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def _crear_pedido_desde_datos(self, pedido_data: dict, gestor_inventario: GestorInventario) -> Pedido:
        mesa_numero = pedido_data['mesa_numero']
        nuevo_pedido = Pedido(mesa_numero)

        for nombre, cantidad in pedido_data['productos'].items():
            producto = gestor_inventario.obtener_producto(nombre)
            if producto:
                nuevo_pedido.agregar_producto(producto, cantidad)
            else:
                print(f"Producto {nombre} no encontrado en el inventario durante la carga de la factura.")

        return nuevo_pedido
