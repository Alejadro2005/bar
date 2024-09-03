from Gestores.gestor_inventario import GestorInventario
from Gestores.gestor_pedidos import GestorPedidos
from Gestores.gestor_mesas import GestorMesas
from Gestores.gestor_sesion import GestorSesion
from Gestores.gestor_facturas import GestorFacturas


def main() -> None:
    # Instanciar gestores
    gestor_inventario = GestorInventario()
    gestor_mesas = GestorMesas()
    gestor_pedidos = GestorPedidos(gestor_inventario, gestor_mesas)
    gestor_sesion = GestorSesion()
    gestor_facturas = GestorFacturas()

    # Cargar inventario desde JSON
    gestor_inventario.cargar_inventario_desde_json('data/inventario.json')

    # Cargar pedidos desde JSON
    gestor_pedidos.cargar_pedidos_desde_json('data/pedidos.json')

    # Opciones de usuario
    while True:
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if gestor_sesion.autenticar(usuario, contrasena):
            if usuario == "admin":
                while True:
                    print("\n--- Menú de Administrador ---")
                    print("1. Visualizar ganancias por propinas")
                    print("2. Evaluar efectividad de meseros")
                    print("3. Mostrar inventario")
                    print("4. Agregar producto al inventario")
                    print("5. Actualizar stock de producto")
                    print("6. Eliminar producto del inventario")
                    print("7. Ver estado de las mesas")
                    print("8. Ver nombres de los meseros")
                    print("9. Ver historial de facturas")
                    print("10. Salir")
                    opcion_admin = input("Seleccione una opción: ")

                    if opcion_admin == "1":
                        print("\n--- Ganancias por Propinas ---")
                        total_propinas = sum(mesero.propinas_acumuladas for mesero in gestor_sesion.meseros)
                        print(f"Total de ganancias por propinas: ${total_propinas:.2f}")
                    elif opcion_admin == "2":
                        print("\n--- Evaluación de Efectividad de Meseros ---")
                        for mesero in gestor_sesion.meseros:
                            print(mesero)
                    elif opcion_admin == "3":
                        print("\n--- Inventario ---")
                        gestor_inventario.mostrar_inventario()
                    elif opcion_admin == "4":
                        nombre = input("Nombre del producto: ")
                        precio = float(input("Precio: "))
                        stock = int(input("Stock: "))
                        tipo = input("Tipo (plato/bebida): ")
                        categoria = input("Categoría (opcional): ")
                        tamaño = input("Tamaño (opcional): ")
                        gestor_inventario.agregar_producto(nombre, precio, stock, tipo, categoria, tamaño)
                        print(f"Producto {nombre} agregado al inventario.")
                    elif opcion_admin == "5":
                        nombre = input("Nombre del producto: ")
                        stock = int(input("Nuevo stock: "))
                        gestor_inventario.actualizar_stock(nombre, stock)
                        print(f"Stock del producto {nombre} actualizado a {stock}.")
                    elif opcion_admin == "6":
                        nombre = input("Nombre del producto a eliminar: ")
                        gestor_inventario.eliminar_producto(nombre)
                        print(f"Producto {nombre} eliminado del inventario.")
                    elif opcion_admin == "7":
                        print("\n--- Estado de las Mesas ---")
                        gestor_mesas.mostrar_mesas()
                    elif opcion_admin == "8":
                        print("\n--- Nombres de los Meseros ---")
                        nombres_meseros = gestor_sesion.obtener_meseros()
                        for nombre in nombres_meseros:
                            print(nombre)
                    elif opcion_admin == "9":
                        print("\n--- Historial de Facturas ---")
                        gestor_facturas.mostrar_facturas()
                    elif opcion_admin == "10":
                        break
                    else:
                        print("Opción no válida.")
            elif usuario.startswith("mesero"):
                while True:
                    print("\n--- Menú de Mesero ---")
                    print("1. Registrar pedido")
                    print("2. Entregar pedido")
                    print("3. Ver propinas acumuladas")
                    print("4. Salir")
                    opcion_mesero = input("Seleccione una opción: ")

                    if opcion_mesero == "1":
                        mesa_numero = int(input("Número de mesa: "))
                        productos = {}
                        while True:
                            nombre = input("Nombre del producto (o 'done' para terminar): ")
                            if nombre == 'done':
                                break
                            cantidad = int(input("Cantidad: "))
                            productos[nombre] = cantidad
                        try:
                            gestor_pedidos.crear_pedido(mesa_numero, productos)
                            print("Pedido registrado exitosamente.")
                        except ValueError as e:
                            print(e)
                    elif opcion_mesero == "2":
                        mesa_numero = int(input("Número de mesa: "))
                        propina = float(input("Propina: "))
                        try:
                            factura = gestor_pedidos.generar_factura(mesa_numero, propina)
                            mesero = gestor_sesion.obtener_mesero(usuario)
                            mesero.agregar_propina(propina)
                            gestor_facturas.agregar_factura(factura)
                            print("Factura generada:")
                            print(factura)
                        except ValueError as e:
                            print(e)
                    elif opcion_mesero == "3":
                        mesero = gestor_sesion.obtener_mesero(usuario)
                        print(f"Propinas acumuladas: ${mesero.propinas_acumuladas:.2f}")
                    elif opcion_mesero == "4":
                        break
                    else:
                        print("Opción no válida.")
        else:
            print("Usuario o contraseña incorrectos.")


if __name__ == "__main__":
    main()
