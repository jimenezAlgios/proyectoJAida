

class ListaJugadores:
    listaJ = []
    numJugadores = 0
    #constructor:
    def __init__(self):
        self.listaJ=[]
      
    def addJugador(self):
        
        print "Inserta nombre de jugador"
        
        nombre = input()
        jugador = Jugador(nombre)
        
        #print jugador.
        
        #mirar si existe
        if lista.index( nombre )==null: 
            listaJ.append(jugador)
            numJugadores = numJugadores +1
        else:
            print "El nombre ya existe"
            addJugador ()
            
    def imprimirPuntuacion(self):
        
        for i in range(numJugadores):
            
            jugador = Jugador(ListaJugadores.listaJ[i])  
            jugador.imprimirPuntuacion() 
            
            
