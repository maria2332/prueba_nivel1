import csv
import configuracion 

class vehiculo():
    def __init__(self, color, ruedas):
        self.color = color 
        self.ruedas = ruedas
    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)
    


class Coche(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
            return super().__str__() + ", Velocidad: " + str(self.velocidad) + ", Cilindrada: " + str(self.cilindrada)
    
class Bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
             return super().__str__() + ", Tipo: " + str(self.tipo)  


class camioneta(Coche):
     def __init__(self, color, ruedas, velocidad, cilindrada, carga):
          super().__init__(color, ruedas, velocidad, cilindrada)
          self.carga = carga
     def __str__(self):
            return super().__str__() + ", Carga: " + str(self.carga)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
            return super().__str__() + ", Velocidad: " + str(self.velocidad) + ", Cilindrada: " + str(self.cilindrada)
     
 
class Quad(Bicicleta, Coche):
    def __init__(self, color, ruedas, modelo, carga):
        super.__init__(color, ruedas) and Bicicleta.__init__(color, ruedas)
        self.modelo = modelo
        self.carga = carga
    def __str__(self):
            return super().__str__() + ", Velocidad: " + str(self.modelo) + ", Cilindrada: " + str(self.carga)
    

# def catalogar(lista_vehiculos):
#     for vehiculo in lista_vehiculos:
#         print (vehiculo)
#         ruedas = vehiculo.ruedas
#         if ruedas == 2:
#             print("Es una bicicleta o una motocicleta")
#         elif ruedas == 4:
#             print("Es un coche o una camioneta")
#         else:
#             print("No es un vehículo")
#     return lista_vehiculos   

c = Coche("azul", 4, 150, 1200)
print(c)

b = Bicicleta("roja", 2, "urbana")
print(b)

m = Motocicleta("negra", 2, "urbana", 200, 600)
print(m)

cam = camioneta("blanca", 4, 100, 2000, 1000)
print(cam)

q = Quad("verde", 4, "panda", 1200)
print(q)

# lista_vehiculos = [Coche("azul", 4, 150, 1200), Bicicleta("roja", 2, "urbana"), Motocicleta("negra", 2, "urbana", 200, 600), camioneta("blanca", 4, 100, 2000, 1000)]


# catalogar(lista_vehiculos)  
