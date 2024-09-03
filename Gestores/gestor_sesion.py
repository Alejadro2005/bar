from typing import List
from Modelos.mesero import Mesero


class GestorSesion:
    def __init__(self) -> None:
        self.meseros: List[Mesero] = []
        self.admin_usuario = "admin"
        self.admin_contraseña = "adminpass"
        self.cargar_meseros()

    def cargar_meseros(self) -> None:
        # Agregar meseros por defecto
        self.meseros.append(Mesero("mesero:juan"))
        self.meseros.append(Mesero("mesero:laura"))
        self.meseros.append(Mesero("mesero:diana"))
        self.meseros.append(Mesero("mesero:jose"))
        self.meseros.append(Mesero("mesero:alejo"))

    def autenticar(self, usuario: str, contraseña: str) -> bool:
        return usuario == self.admin_usuario and contraseña == self.admin_contraseña or usuario in [m.nombre for m in
                                                                                                    self.meseros]

    def obtener_meseros(self) -> List[str]:
        return [mesero.nombre for mesero in self.meseros]

    def obtener_mesero(self, nombre: str) -> Mesero:
        for mesero in self.meseros:
            if mesero.nombre == nombre:
                return mesero
        raise ValueError(f"Mesero {nombre} no encontrado.")
