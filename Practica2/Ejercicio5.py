
def clasificar_tiempo (ms: int):
    if (ms < 200):
        return 'Rapido'
    if ms >= 200 and ms <= 500:
         return 'Normal'
    return 'Lento'



tiempo_de_reaccion = int(input('Ingrese su tiempo de reaccion en ms: '))
print (f'Categoria: {clasificar_tiempo(tiempo_de_reaccion)}')