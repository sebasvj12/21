import random

# Funciones para generar la baraja ordenada aleatoriamente
def generar_palo():
    return range(1,11) + ['J', 'K', 'Q']

def generar_palos(palos):
    if palos == 0:
        return []
    else:
        return generar_palo() + generar_palos(palos - 1)   

def mezclar_baraja(mazo):
    random.shuffle(mazo)
    return mazo

def obtener_baraja():
    return mezclar_baraja(generar_palos(4))

# Funcion para imprimir un conjunto de cartas
def imprimir_cartas(cartas):
    print [str(carta) if carta != 1 else "1/11" for carta in cartas ]

def valor_carta(carta):
    if carta == 'A':
        return 1
    elif carta in ['J','Q','K']:
        return 10
    else:
        return carta

def valor_mano(lista):
    if lista == []:
        return 0
    else:
        return valor_carta(lista[0]) + valor_mano(lista[1:])


# Funciones para obtener los puntajes
def obtener_mejor_puntaje(cartas, ases):
    if ases == 0:
        return valor_mano(cartas)
    elif valor_mano(cartas) + 10 * ases <= 21:
        return valor_mano(cartas) + 10 * ases;
    else:
        return obtener_mejor_puntaje(cartas, ases - 1)

def obtener_puntaje(cartas):
    return obtener_mejor_puntaje(cartas, cartas.count(1))

# Funciones para jugar los turnos
def jugar_turno_jugador(cartas):
    print "Sus cartas son:"
    imprimir_cartas(cartas[0])
    print "Las cartas del repartidor son:"
    imprimir_cartas(cartas[1])
    if obtener_puntaje(cartas[0]) < 21 and bool(input("Si quiere pedir mas cartas ingrese 1. De lo contrario 0: ")):
        return jugar_turno_jugador([cartas[0] + [cartas[2][0]]] + [cartas[1]] + [cartas[2][1:]])
    else:
        return cartas
#17 ->20 modificado
def jugar_turno_repartidor(cartas):
    if obtener_puntaje(cartas[1]) < 20 and (obtener_puntaje(cartas[1]) < obtener_puntaje(cartas[0]) and obtener_puntaje(cartas[0]) <=21):
        return jugar_turno_repartidor([cartas[0]] + [cartas[1] + [cartas[2][0]]] + [cartas[2][1:]])            
    else:
        return cartas

# Funcion para imprimir el resultado del juego segun puntajes
def imprimir_resultado(puntaje_jugador, puntaje_repartidor):
    print "Puntaje jugador: " + str(puntaje_jugador) + ". Puntaje repartidor: " + str(puntaje_repartidor)
    if puntaje_jugador > 21 and puntaje_jugador > puntaje_repartidor:
        print "Jugador PIERDE el juego."
    elif puntaje_jugador == 21 and (puntaje_repartidor > 21 or puntaje_repartidor < 21):
        print "Jugador GANA el juego."
    elif puntaje_jugador == 21 and puntaje_repartidor == 21:
        print "Igualados, el Jugador PIERDE el juego."
    elif puntaje_jugador < 21 and (puntaje_repartidor > 21 or puntaje_repartidor < puntaje_jugador):
        print "Jugador GANA el juego."
    elif puntaje_jugador < 21 and puntaje_repartidor > puntaje_jugador:
        print "Jugador PIERDE el juego."
    elif (puntaje_jugador > 21 and puntaje_repartidor >21) and puntaje_jugador < puntaje_repartidor :
        print "el jugador estuvo mas serca"
    else:
        print "Igualados, el Jugador PIERDE el juego..."    

# Funcion que guia el desarrollo del juego
def black_jack(cartas, turnoJugadorHecho, turnoRepartidorHecho):
    if cartas[2] == []:
        print "\nPreparando la baraja..."
        black_jack(cartas[0:2] + [obtener_baraja()], turnoJugadorHecho, turnoRepartidorHecho)
    elif cartas[0] == []:
        print "\nRepartiendo cartas al jugador..."
        black_jack([cartas[2][0:2]] + [cartas[1]] + [cartas[2][2:]], turnoJugadorHecho, turnoRepartidorHecho)
    elif cartas[1] == []:
        print "\nColocando carta del repartidor..."
        black_jack([cartas[2][0:2]] + [cartas[0]] + [cartas[2][1:]], turnoJugadorHecho, turnoRepartidorHecho)
    elif not turnoJugadorHecho:
        print "\n** COMIENZO TURNO JUGADOR:\n"
        black_jack(jugar_turno_jugador(cartas), True, turnoRepartidorHecho)
    elif not turnoRepartidorHecho:
        print "\n** COMIENZO TURNO REPARTIDOR...\n"
        black_jack(jugar_turno_repartidor(cartas), turnoJugadorHecho, True)        
    else:
        print "Las cartas finales del repartidor son:"
        imprimir_cartas(cartas[1])
        print "\n** RESULTADO DEL JUEGO:\n"        
        imprimir_resultado(obtener_puntaje(cartas[0]), obtener_puntaje(cartas[1]))        

# Funcion de inicio
def jugar_black_jack():
    print "BIENVENIDO AL JUEGO 21:"
    black_jack([[], [], []], False, False)
    print "\nJUEGO TERMINADO."

# Iniciar juego
jugar_black_jack()  
