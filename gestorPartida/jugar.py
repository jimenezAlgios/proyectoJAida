import random
from gestorJugador.Jugador import Jugador

def jugarPartida(nombre):  
    print "empieza el juego"
    jugador=Jugador(nombre)
    
    #while
    while jugador.vida > 0:
        numero=random.randint(0, 20)
        print jugador.nombre + " ha recibido un dano de: " ,numero, " puntos"
        jugador.actualizarVida(numero)
        print "Le quedan: " , jugador.vida , " puntos de vida"
        jugador.actualizarPuntos(numero)
        
        if jugador.vida < numero:
            jugador.vida=0
        
        if jugador.vida == 0 :
            
            print "Fin del juego, has muerto"
            jugador.imprimirPuntuacion()
        
    
    
    
    
    
   
    