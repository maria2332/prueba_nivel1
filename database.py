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
        vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
            return vehiculo.__str__(self) + ", Velocidad: " + str(self.velocidad) + ", Cilindrada: " + str(self.cilindrada)
    
class Bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
             return vehiculo.__str__(self) + ", Tipo: " + str(self.tipo)  



class camioneta(Coche):
     def __init__(self, color, ruedas, velocidad, cilindrada, carga):
          Coche.__init__(self, color, ruedas, velocidad, cilindrada)
          self.carga = carga
     def __str__(self):
            return Coche.__str__(self) + ", Carga: " + str(self.carga)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        vehiculo.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
            return vehiculo.__str__(self) + ", Velocidad: " + str(self.velocidad) + ", Cilindrada: " + str(self.cilindrada)
     
 
def catalogar(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        print (vehiculo)
    return lista_vehiculos   

# c = Coche("azul", 4, 150, 1200)
# print(c)

# b = Bicicleta("roja", 2, "urbana")
# print(b)

# m = Motocicleta("negra", 2, "urbana", 200, 600)
# print(m)

# cam = camioneta("blanca", 4, 100, 2000, 1000)
# print(cam)

lista_vehiculos = [Coche("azul", 4, 150, 1200), Bicicleta("roja", 2, "urbana"), Motocicleta("negra", 2, "urbana", 200, 600), camioneta("blanca", 4, 100, 2000, 1000)]


catalogar(lista_vehiculos)  
