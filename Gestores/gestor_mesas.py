from typing import List
from Modelos.mesa import Mesa


class GestorMesas:
    def __init__(self) -> None:
        self.mesas: List[Mesa] = [Mesa(i + 1) for i in range(10)]  # Inicializa 10 mesas

    def obtener_mesa(self, numero: int) -> Mesa:
        for mesa in self.mesas:
            if mesa.numero == numero:
                return mesa
        return None

    def mostrar_mesas(self) -> None:
        for mesa in self.mesas:
            estado = "Ocupada" if mesa.ocupada else "Libre"
            print(f"Mesa {mesa.numero}: {estado}")

    def marcar_mesa_ocupada(self, numero: int) -> None:
        mesa = self.obtener_mesa(numero)
        if mesa:
            mesa.ocupada = True

    def marcar_mesa_libre(self, numero: int) -> None:
        mesa = self.obtener_mesa(numero)
        if mesa:
            mesa.ocupada = False
