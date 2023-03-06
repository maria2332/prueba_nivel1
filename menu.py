import os
import helpers
import database as db


def iniciar(): #creamos la función iniciar
    while True: 
        helpers.limpiar_pantalla() #limpiamos la pantalla

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los vehiculos ")
        print("[2] Buscar un vehiculo   ")
        print("[3] Añadir un vehiculo   ")
        print("[4] Modificar un vehiculo")
        print("[5] Borrar un vehiculo   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla() 

        if opcion == '1': 
            print("Listando los vehiculos...\n")
            for vehiculo in db.vehiculos.lista: #recorremos la lista de vehiculos
                print(vehiculo)

        elif opcion == '2':
            print("Buscando un vehiculo...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper() #leemos el DNI
            vehiculo = db.vehiculos.buscar(dni) #buscamos el vehiculo
            print(vehiculo) if vehiculo else print("vehiculo no encontrado.")

        elif opcion == '3':
            print("Añadiendo un vehiculo...\n")

            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()  # Leemos el DNI
                if helpers.dni_valido(dni, db.vehiculos.lista):  # Comprobamos que el DNI sea válido
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize() #leemos el nombre y lo capitalizamos
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize() #leemos el apellido y lo capitalizamos
            db.vehiculos.crear(dni, nombre, apellido) #creamos el vehiculo
            print("vehiculo añadido correctamente.")

        elif opcion == '4':
            print("Modificando un vehiculo...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper() # Leemos el DNI del vehiculo a modificar y lo capitalizamos
            vehiculo = db.vehiculos.buscar(dni) #buscamos el vehiculo
            if vehiculo:
                nombre = helpers.leer_texto(    #leemos el nombre y lo capitalizamos 
                    2, 30, f"Nombre (de 2 a 30 chars) [{vehiculo.nombre}]").capitalize()
                apellido = helpers.leer_texto( #leemos el apellido y lo capitalizamos
                    2, 30, f"Apellido (de 2 a 30 chars) [{vehiculo.apellido}]").capitalize()
                db.vehiculos.modificar(vehiculo.dni, nombre, apellido)
                print("vehiculo modificado correctamente.")
            else:
                print("vehiculo no encontrado.")

        elif opcion == '5':
            print("Borrando un vehiculo...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper() # Leemos el DNI del vehiculo a borrar y lo capitalizamos
            print("vehiculo borrado correctamente.") if db.vehiculos.borrar(   #borramos el vehiculo
                dni) else print("vehiculo no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")