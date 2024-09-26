from bar import *

def main() -> None:
    # Instanciar los gestores
    gestor_inventario = GestorInventario()
    gestor_mesas = GestorMesas()
    gestor_pedidos = GestorPedidos(gestor_inventario, gestor_mesas)
    gestor_sesion = GestorSesion()
    gestor_meseros = GestorMeseros()  # Instanciar GestorMeseros
    gestor_facturas = GestorFacturas()

    # Cargar inventario desde JSON
    gestor_inventario.cargar_inventario_desde_json('data/inventario.json')

    # Cargar pedidos desde JSON
    gestor_pedidos.cargar_pedidos_desde_json('data/pedidos.json')

    # Opciones de usuario
    while True:
        usuario = input("Ingrese su usuario: ")  # No es necesario convertir a minúsculas aquí
        contrasena = input("Ingrese su contraseña: ")

        if gestor_sesion.autenticar(usuario, contrasena):
            if usuario.lower() == "admin":  # Aquí también puedes convertir a minúsculas
                menu_admin(gestor_inventario, gestor_mesas, gestor_facturas, gestor_meseros)
            elif usuario.lower().startswith("mesero:"):
                menu_mesero(gestor_pedidos, gestor_meseros, gestor_facturas, usuario)
        else:
            print("Usuario o contraseña incorrectos.")


# Ejecutar la aplicación
if __name__ == "__main__":
    main()
