from typing import List
from Modelos.factura import Factura

class GestorFacturas:
    def __init__(self) -> None:
        self.facturas: List[Factura] = []

    def agregar_factura(self, factura: Factura) -> None:
        self.facturas.append(factura)

    def mostrar_facturas(self) -> None:
        for factura in self.facturas:
            print(factura)
