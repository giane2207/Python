titles = [
        "Speedrun de Super Mario en tiempo récord", 
        "Charla sobre desarrollo de videojuegos",
        "Jugando al nuevo FPS del momento con amigos",
        "Música en vivo: improvisaciones al piano"
        ]

# Busca el maximo de la lista de acuerdo a la longitud del string
titulo_mas_largo = max(titles, key=len)

#titulo_mas_largo = max(titles)

print(titulo_mas_largo)