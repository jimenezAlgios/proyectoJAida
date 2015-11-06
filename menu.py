from jugar import jugarPartida

import sys

def imprimirMenu():
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
    
    num=0
    num = input()
    
    
    '''
    a = int(raw_input('dame un numero'))
>     sys.exit(0)
>
> # Si el dato no es un numero entero ejecutamos la salida con codigo 1
> (terminacion anormal)
> # si quisieramos salir tras una ejecucion correcta seria con codigo 0.
> except:
>     sys.exit(1)
    '''
    
    if num==1:
        jugarPartida()
    
    #elseif num==2:
        #ListaJugadores.addJugador()
    #else:
       # if numm=3:
      #  ListaJugadores.mostrarEstadisticas()
    elif num == 4:
        print "bye byeee"
        sys.exit()
            
        
        
        
        
        