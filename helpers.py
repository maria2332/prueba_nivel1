import re
import os
import platform


def limpiar_pantalla(): # Función para limpiar la pantalla
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None): # Función para leer texto
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max: # Comprobamos que el texto cumpla las restricciones de longitud
            return texto


def numeroBastidor_valido(numeroBastidor, lista): # Función para validar el numeroBastidor
    if not re.match('[0-9]{2}[A-Z]$', numeroBastidor): # Comprobamos que el numeroBastidor cumpla el formato
        print("numeroBastidor incorrecto, debe cumplir el formato.")
        return False
    for vehiculo in lista: # Comprobamos que el numeroBastidor no esté utilizado por otro vehiculo
        if vehiculo.numeroBastidor == numeroBastidor: 
            print("numeroBastidor utilizado por otro vehiculo.")
            return False
    return True