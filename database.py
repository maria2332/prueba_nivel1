import csv
import configuracion 

class vehiculo():
    def __init__(self, color, ruedas, numeroBastidor):
        self.color = color 
        self.ruedas = ruedas
        self.numeroBastidor = numeroBastidor
    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas) + ", ID: " + str(self.numeroBastidor)
    


class Coche(vehiculo):
    def __init__(self, numeroBastidor, color, ruedas, velocidad, cilindrada):
        super().__init__(numeroBastidor,color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
            return super().__str__() + ", Velocidad: " + str(self.velocidad) + ", Cilindrada: " + str(self.cilindrada)
    
class Bicicleta(vehiculo):
    def __init__(self, numeroBastidor,color, ruedas, tipo):
        super().__init__(numeroBastidor,color, ruedas)
        self.tipo = tipo
    def __str__(self):
             return super().__str__() + ", Tipo: " + str(self.tipo)  


class camioneta(Coche):
     def __init__(self, numeroBastidor, color, ruedas, velocidad, cilindrada, carga):
          super().__init__(numeroBastidor, color, ruedas, velocidad, cilindrada)
          self.carga = carga
     def __str__(self):
            return super().__str__() + ", Carga: " + str(self.carga)


class Formula1(Coche):
     def __init__(self, numeroBastidor,color, ruedas, velocidad, cilindrada, escuderia):
          super().__init__(numeroBastidor, color, ruedas, velocidad, cilindrada)
          self.escuderia = escuderia
     def __str__(self):
            return super().__str__() + ", Neumaticos: " + str(self.escuderia)
     

class Motocicleta(Bicicleta):
    def __init__(self, numeroBastidor, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(numeroBastidor, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
            return super().__str__() + ", Velocidad: " + str(self.velocidad) + ", Cilindrada: " + str(self.cilindrada)
     
 
class Quad(Coche):
    def __init__(self, numeroBastidor, color, ruedas, tipo, velocidad, cilindrada, modelo, carga):
        super().__init__(numeroBastidor, color, ruedas, velocidad, cilindrada) 
        self.modelo = modelo
        self.carga = carga
        self.tipo = tipo
    def __str__(self):
            return super().__str__() + ", Modelo: " + str(self.modelo) + ", Carga: " + str(self.carga) + ", Tipo: " + str(self.tipo)
    

c = Coche("azul", 4, "asdsf", 150, 1200)
print(c)

b = Bicicleta("roja", 2, "wqref", "urbana")
print(b)

m = Motocicleta("negra", 2, "jmskl", "urbana", 200, 600)
print(m)

cam = camioneta("blanca", 4, "ahksa", 100, 2000, 1000)
print(cam)

q = Quad("negra", 4, "jmskl", "urbana", 200, 600, "panda", 100)
print(q)

# lista_vehiculos = [c, b, m, cam]

# def catalogar(lista_vehiculos):
#     for vehiculo in lista_vehiculos:
#         print (vehiculo)
#         ruedas = vehiculo.ruedas
#         if ruedas == 2:
#             if isinstance(vehiculo, Bicicleta):
#                 print("Es una bicicleta")
#             elif isinstance(vehiculo, Motocicleta):
#                 print("Es una motocicleta")
#         elif ruedas == 4:
#             if isinstance(vehiculo, Coche):
#                 print("Es un coche")
#             elif isinstance(vehiculo, camioneta):
#                 print("Es una camioneta")           
#         else:
#             print("No es un vehículo")
#     return lista_vehiculos

# catalogar(lista_vehiculos)



# class vehiculos:

#     lista = []
#     with open(config.DATABASE_PATH, newline='\n') as fichero:   
#         reader = csv.reader(fichero, delimiter=';')
#         for numeroBastidor, nombre, apellido in reader:
#             vehiculo = vehiculo(numeroBastidor, nombre, apellido)
#             lista.append(vehiculo)

#     @staticmethod #creamos el método estático buscar
#     def buscar(numeroBastidor):
#         for vehiculo in vehiculos.lista:
#             if vehiculo.numeroBastidor == numeroBastidor:
#                 return vehiculo

#     @staticmethod #creamos el método estático crear
#     def crear(numeroBastidor, nombre, apellido):
#         vehiculo = vehiculo(numeroBastidor, nombre, apellido)
#         vehiculos.lista.append(vehiculo)
#         vehiculos.guardar()
#         return vehiculo

#     @staticmethod #creamos el método estático modificar
#     def modificar(numeroBastidor, nombre, apellido):
#         for indice, vehiculo in enumerate(vehiculos.lista):
#             if vehiculo.numeroBastidor == numeroBastidor:
#                 vehiculos.lista[indice].nombre = nombre
#                 vehiculos.lista[indice].apellido = apellido
#                 vehiculos.guardar()
#                 return vehiculos.lista[indice]

#     @staticmethod #creamos el método estático borrar
#     def borrar(numeroBastidor):
#         for indice, vehiculo in enumerate(vehiculos.lista):
#             if vehiculo.numeroBastidor == numeroBastidor:
#                 vehiculo = vehiculos.lista.pop(indice)
#                 vehiculos.guardar()
#                 return vehiculo

#     @staticmethod #creamos el método estático guardar
#     def guardar():
#         with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
#             writer = csv.writer(fichero, delimiter=';')
#             for vehiculo in vehiculos.lista:
#                 writer.writerow((vehiculo.numeroBastidor, vehiculo.nombre, vehiculo.apellido))
     