from gestorJugador.Jugador import Jugador

class ListaJugadores:
    listaJ = []
    numJugadores = 0
    #constructor:
    def __init__(self):
        self.listaJ=[]
      
    def addJugador(self):
        
        print "Inserta nombre de jugador"
        
        nombre = raw_input()
        jugador = Jugador(nombre)
        lista=ListaJugadores.listaJ
        numJugadores=ListaJugadores.numJugadores
        #prueba 
        print numJugadores
        
        #mirar si existe
        if lista.index( nombre )==None: 
            lista.append(jugador)
            numJugadores = numJugadores +1
        else:
            print "El nombre ya existe"
            ListaJugadores.addJugador()
            
    def imprimirPuntuacion(self):
        
        for i in range(ListaJugadores.numJugadores):
            
            jugador = Jugador(ListaJugadores.listaJ[i])  
            jugador.imprimirPuntuacion() 
            
            
