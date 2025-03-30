descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"
]

#Inicializo mi diccionario
menciones = {'música': 0, 'charla': 0, 'entretenimiento': 0}

# Por cada descripcion busco si hay alguna mencion y la incremento
for desc in descriptions:
    for mencion in menciones:
        if (mencion in desc):
            menciones[mencion] += 1

for k, v in menciones.items():
    print(f'Menciones de {k}: {v}')