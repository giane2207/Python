import utils
from data import *


# Diccionario con datos de todos los jugadores
ranking = {}

# Recorro cada ronda 
for ronda in rounds:

    # Diccionario para guardar la puntuación de cada jugador de la ronda actual
    points_round = {}

    # Recorro cada jugador de la ronda
    for jugador, datos in ronda.items():  

        # Si el jugador no está en el ranking, inicializo sus datos
        utils.inicializar_jugador
        
        # Actualizo los datos del jugador en el ranking
        utils.actualizar_jugador(jugador, ranking, datos)
        
        # Calculo los puntos de la ronda actual
        puntos = utils.calcular_puntos(datos, scoring) 
        
        # Actualiza los puntos en el ranking y la tabla de puntajes
        ranking[jugador]['points'] += puntos
        points_round[jugador] = puntos

    # Guardo el MVP de la ronda
    MVP = max(points_round, key=points_round.get)
    ranking[MVP]['MVPs'] += 1

    # Muestro el ranking parcial
    print("\nRanking Parcial:")
    utils.imprimir_ranking(ranking)
    print("\n" + "="*40)  # Línea separadora entre rondas

# Muestro el ranking final
print("\nRanking Final:")
utils.imprimir_ranking(ranking)