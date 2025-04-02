
def imprimir_ranking(ranking_ordenado):
    """Imprime de manera ordenada el contenido del ranking"""
    print("Pos. Jugador   K   A   D  Puntos  MVPs")
    print("-------------------------------------")
    
    for pos, (jugador, stats) in enumerate(ranking_ordenado, start=1):
        print(f"{pos:<4} {jugador:<10} {stats['kills']:<3} {stats['assists']:<3} {stats['deaths']:<3} {stats['points']:<7} {stats['MVPs']:<3}")     

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
    puntos = datos['kills'] * scoring['kill']
    puntos += datos['assists'] * scoring['assist']
    if datos['deaths']:
         puntos -= scoring['death'] 
    return puntos