import sys
import gestorJugador.ListaJugadores
import gestorPartida.jugar

def imprimirMenu():
    
    listaJ=gestorJugador.ListaJugadores.ListaJugadores()
    
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "********* Elige una opcion*********"
    print "1.jugar                            "
    print "2.Anadir Jugador                   "
    print "3.mostrar estadisticas jugador     "
    print "4.Salir                            "
    print "***********************************"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
   
    
    #num=0
    num = input()
   
    if num==1:
        print "inserta nombre jugador"
        nombre=input()
        gestorPartida.jugar.jugarPartida(nombre)
    
    elif num==2:
        print "prueba punto 2"
        listaJ.addJugador()  
        
    #elif num==3      
      #  ListaJugadores.mostrarEstadisticas()
    elif num == 4:
        print "bye byeee"
        sys.exit()
    
            
        
        
        
        
        