import utils
from data import *


# Diccionario con datos de todos los jugadores
ranking = {}

# Recorro cada ronda 
for ronda in rounds:

    # Se guarda la puntuación de la ronda actual
    points_round = {}

    # Recorro cada jugador de la ronda
    for jugador, datos in ronda.items():  

        # Si el jugador no está en el ranking, inicializo sus datos
        if jugador not in ranking:  
            ranking[jugador] = {
                'kills': 0,
                'assists': 0,
                'deaths': 0,
                'MVPs': 0,
                'points': 0
            }
        
        # Actualizo los datos del jugador en el ranking
        ranking[jugador]['kills'] += datos['kills']
        ranking[jugador]['assists'] += datos['assists']
        ranking[jugador]['deaths'] += int(datos['deaths']) # Convierte true en 1, false en 0

        # Calculo los puntos de la ronda actual
        puntos = datos['kills'] * scoring['kill']
        puntos += datos['assists'] * scoring['assist']
        if datos['deaths']:
            puntos -= scoring['death']  
        
        ranking[jugador]['points'] += puntos
        points_round[jugador] = puntos

    # Guardo el MVP de la ronda
    MVP = max(points_round, key=points_round.get)
    ranking[MVP]['MVPs'] += 1

    # Ordeno y muestro el ranking parcial
    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1]['points'], reverse=True)
    print("\nRanking Parcial:")
    utils.imprimir_ranking(ranking_ordenado)
    print("\n" + "="*40)  # Línea separadora entre rondas

# Ordeno y muestro el ranking final
ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1]['points'], reverse=True)
print("\nRanking Final:")
utils.imprimir_ranking(ranking_ordenado)