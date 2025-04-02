from src.utils import *

def simulador_partidas (rounds, scoring):
    """Simula todas las rondas y muestra los rankings parciales y final"""
    ranking = {}

    for ronda in rounds:

         points_round = {}

         for jugador, datos in ronda.items():  
             #Inicializar jugador si no esta en el ranking
             utils.inicializar_jugador(jugador, ranking)
            
             # Actualizo los datos del jugador
             utils.actualizar_jugador(jugador, ranking, datos)
            
             # Calculo puntos obtenidos en esta ronda
             puntos = utils.calcular_puntos(datos, scoring) 
             ranking[jugador]['points'] += puntos
             points_round[jugador] = puntos

         # Determino y guardo el MVP de la ronda
         MVP = max(points_round, key=points_round.get)
         ranking[MVP]['MVPs'] += 1

         # Muestro el ranking parcial
         print("\nRanking Parcial:")
         print(utils.imprimir_ranking(ranking))

    # Muestro el ranking final
    print("\nRanking Final:")
    print(utils.imprimir_ranking(ranking))