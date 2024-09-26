from typing import List

class GestorSesion:
    def __init__(self) -> None:
        self.admin_usuario = "admin"
        self.admin_contraseña = "adminpass"
        self.meseros: List[str] = ["mesero:juan", "mesero:laura", "mesero:diana", "mesero:jose", "mesero:alejo"]

    def autenticar(self, usuario: str, contraseña: str) -> bool:
        # Convertir el nombre de usuario a minúsculas
        usuario = usuario.lower()
        # Autenticar meseros o administrador
        return (usuario == self.admin_usuario and contraseña == self.admin_contraseña) or usuario in (mesero.lower() for mesero in self.meseros)
