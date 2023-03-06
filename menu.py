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
            numeroBastidor = helpers.leer_texto(3, 3, "numeroBastidor (2 int y 1 char)").upper() #leemos el numeroBastidor
            vehiculo = db.vehiculos.buscar(numeroBastidor) #buscamos el vehiculo
            print(vehiculo) if vehiculo else print("vehiculo no encontrado.")

        elif opcion == '3':
            print("Añadiendo un vehiculo...\n")

            numeroBastidor = None
            while True:
                numeroBastidor = helpers.leer_texto(3, 3, "numeroBastidor (2 int y 1 char)").upper()  # Leemos el numeroBastidor
                if helpers.numeroBastidor_valido(numeroBastidor, db.vehiculos.lista):  # Comprobamos que el numeroBastidor sea válido
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize() #leemos el nombre y lo capitalizamos
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize() #leemos el apellido y lo capitalizamos
            db.vehiculos.crear(numeroBastidor, nombre, apellido) #creamos el vehiculo
            print("vehiculo añadido correctamente.")

        elif opcion == '4':
            print("Modificando un vehiculo...\n")
            numeroBastidor = helpers.leer_texto(3, 3, "numeroBastidor (2 int y 1 char)").upper() # Leemos el numeroBastidor del vehiculo a modificar y lo capitalizamos
            vehiculo = db.vehiculos.buscar(numeroBastidor) #buscamos el vehiculo
            if vehiculo:
                nombre = helpers.leer_texto(    #leemos el nombre y lo capitalizamos 
                    2, 30, f"Nombre (de 2 a 30 chars) [{vehiculo.nombre}]").capitalize()
                apellido = helpers.leer_texto( #leemos el apellido y lo capitalizamos
                    2, 30, f"Apellido (de 2 a 30 chars) [{vehiculo.apellido}]").capitalize()
                db.vehiculos.modificar(vehiculo.numeroBastidor, nombre, apellido)
                print("vehiculo modificado correctamente.")
            else:
                print("vehiculo no encontrado.")

        elif opcion == '5':
            print("Borrando un vehiculo...\n")
            numeroBastidor = helpers.leer_texto(3, 3, "numeroBastidor (2 int y 1 char)").upper() # Leemos el numeroBastidor del vehiculo a borrar y lo capitalizamos
            print("vehiculo borrado correctamente.") if db.vehiculos.borrar(   #borramos el vehiculo
                numeroBastidor) else print("vehiculo no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")