
def son_anagramas (palabra1: str, palabra2: str):
    """Verifica si dos palabras son anagramas"""

    #Elimino espacios en blanco y convierto a minusculas
    palabra1 = palabra1.strip().lower()
    palabra2 = palabra2.strip().lower()

    # Si ordenados son iguales, entonces son anagramas
    return sorted(palabra1) == sorted(palabra2)


p1 = input('Ingrese la primera palabra: ')
p2 = input('Ingrese la segunda palabra: ')

if son_anagramas(p1, p2):
    print('Son anagramas.')
else:
    print('No son anagramas.')