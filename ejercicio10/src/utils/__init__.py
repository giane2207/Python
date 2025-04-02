def inicializar_jugador (jugador, ranking):
    """Inserta nuevos jugadores en el ranking con sus datos incializados"""
    if jugador not in ranking:  
            ranking[jugador] = {
                'kills': 0,
                'assists': 0,
                'deaths': 0,
                'MVPs': 0,
                'points': 0
            }
            
def actualizar_jugador (jugador, ranking, datos):
     """Actualiza los datos de un jugador existente en el ranking"""
     ranking[jugador]['kills'] += datos['kills']
     ranking[jugador]['assists'] += datos['assists']
     ranking[jugador]['deaths'] += int(datos['deaths']) # Convierte true en 1, false en 0


def calcular_puntos (datos, scoring):
    """Calcula los puntos obtenidos del jugador de acuerdo al sistema de puntuacion"""
    puntos = datos['kills'] * scoring['kill']
    puntos += datos['assists'] * scoring['assist']
    if datos['deaths']:
         puntos += scoring['death'] 
    return puntos


def imprimir_ranking(ranking):
    """Devuelve el ranking ordenado en forma de cadena."""
    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1]['points'], reverse=True)

    resultado = "Jugador   Kills   Asistencias   Muertes   MVPs   Puntos\n"
    resultado += "---------------------------------------------------------\n"

    for jugador, stats in ranking_ordenado:
        resultado += f"{jugador:<10} {stats['kills']:<8} {stats['assists']:<12} {stats['deaths']:<9} {stats['MVPs']:<6} {stats['points']:<6}\n"

    resultado += "---------------------------------------------------------"
    return resultado