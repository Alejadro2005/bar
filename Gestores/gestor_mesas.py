from typing import List, Optional
from Modelos.mesa import Mesa

class GestorMesas:
    def __init__(self) -> None:
        # Inicializa 10 mesas numeradas del 1 al 10
        self.mesas: List[Mesa] = [Mesa(i + 1) for i in range(10)]
        self.mesas_ocupadas: set[int] = set()  # Conjunto para gestionar las mesas ocupadas

    def obtener_mesa(self, numero: int) -> Optional[Mesa]:
        """Obtiene una mesa por su número."""
        if numero < 1 or numero > len(self.mesas):
            raise ValueError(f"El número de mesa {numero} es inválido. Debe estar entre 1 y {len(self.mesas)}.")

        return self.mesas[numero - 1]  # Ya que las mesas están indexadas desde 0

    def mostrar_mesas(self) -> None:
        """Muestra el estado de todas las mesas."""
        print("--- Estado de las Mesas ---")
        for i in range(0, len(self.mesas), 5):  # Cambiar 5 si quieres más o menos columnas
            for mesa in self.mesas[i:i + 5]:  # Muestra 5 mesas por fila
                estado = "Ocupada" if mesa.ocupada else "Libre"
                print(f"Mesa {mesa.numero}: {estado}", end="\t")
            print()  # Nueva línea después de cada fila

    def marcar_mesa_ocupada(self, numero: int) -> None:
        """Marca una mesa como ocupada."""
        mesa = self.obtener_mesa(numero)
        if mesa:
            if mesa.ocupada:
                print(f"La mesa {numero} ya está ocupada.")
            else:
                mesa.ocupar()
                self.mesas_ocupadas.add(numero)  # Añade a las ocupadas
                print(f"Mesa {numero} marcada como ocupada.")
        else:
            raise ValueError(f"La mesa {numero} no existe.")

    def marcar_mesa_libre(self, numero: int) -> None:
        """Marca una mesa como libre."""
        mesa = self.obtener_mesa(numero)
        if mesa:
            if not mesa.ocupada:
                print(f"La mesa {numero} ya está libre.")
            else:
                mesa.liberar()
                self.mesas_ocupadas.discard(numero)  # Elimina de las ocupadas
                print(f"Mesa {numero} marcada como libre.")
        else:
            raise ValueError(f"La mesa {numero} no existe.")

    def obtener_mesas_ocupadas(self) -> List[int]:
        """Retorna una lista con los números de las mesas ocupadas."""
        return list(self.mesas_ocupadas)
