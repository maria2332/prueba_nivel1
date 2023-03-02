import helpers
import database as db



def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al catalogador de vehículos  ")
        print("========================")
        print("[1] Listar los vehículos ")
        print("[2] Buscar una camioneta   ")
        print("[3] Añadir un cliente   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los vehículos...\n")
            db.catalogar(db.lista)


        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")