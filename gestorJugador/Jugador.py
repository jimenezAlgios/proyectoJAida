
class Jugador:
    nombre = ""
    vida = 100
    puntuacion= 0

    #constructor
    def __init__(self, nombre):
        self.nombre = nombre
    
     
                
    def imprimirPuntuacion(self):
        print "el jugador " + self.nombre + "tiene: ", self.puntuacion," puntos"

    
    def actualizarPuntos(self,puntos):
        self.puntuacion=self.puntuacion+puntos
    def actualizarVida(self,puntos):
        self.vida=self.vida-puntos