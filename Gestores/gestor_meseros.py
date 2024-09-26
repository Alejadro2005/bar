from typing import List
from Modelos.mesero import Mesero


class GestorMeseros:
    def __init__(self) -> None:
        self.meseros: List[Mesero] = []
        self.cargar_meseros()

    def cargar_meseros(self) -> None:
        # Agregar meseros por defecto
        self.meseros.append(Mesero("mesero:juan"))
        self.meseros.append(Mesero("mesero:laura"))
        self.meseros.append(Mesero("mesero:diana"))
        self.meseros.append(Mesero("mesero:jose"))
        self.meseros.append(Mesero("mesero:alejo"))

    def obtener_mesero(self, nombre: str) -> Mesero:
        """Retorna un mesero por su nombre."""
        for mesero in self.meseros:
            if mesero.nombre == nombre:
                return mesero
        raise ValueError(f"Mesero '{nombre}' no encontrado.")

    def evaluar_efectividad_mesero(self, nombre: str) -> float:
        """Evaluar efectividad basándose en las propinas acumuladas."""
        mesero = self.obtener_mesero(nombre)
        # Por ejemplo, calcular la efectividad como porcentaje
        if mesero.propinas_acumuladas < 0:
            raise ValueError(f"Las propinas acumuladas de '{nombre}' no pueden ser negativas.")

        # Considerar un umbral mínimo para la evaluación
        umbral = 50
        if mesero.propinas_acumuladas > umbral:
            return 100.0  # Muy efectivo
        else:
            return (mesero.propinas_acumuladas / umbral) * 100  # Un porcentaje basado en el umbral
