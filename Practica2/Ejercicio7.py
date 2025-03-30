from datetime import date
import string
import random

def es_valido (user: str):
    """Verifica que el usuario no exceda 15 caracteres y sea alfanumerico"""
    return len(user) <= 15 and user.isalnum()

def generar_codigo (user: str):
    """Genera un codigo de descuento basado en el nombre de usuario y la fecha actual"""
    fecha_actual = date.today().strftime("%Y%m%d")   
    alfanumericos = string.ascii_uppercase + string.digits
    user_mayus = user.upper()
    
    # Calculo cuantos caracteres aleatorios necesito
    restante = 30 - (len(user_mayus) + len(fecha_actual) + 2) 

    # Genero la parte aleatoria
    parte_aleatoria = ''.join(random.choices(alfanumericos, k=restante))

    codigo = f'{user_mayus}-{fecha_actual}-{parte_aleatoria}'
    return codigo
    

user = input('Ingrese nombre de usuario: ')

if es_valido(user):
    print(f'Codigo de descuento: {generar_codigo(user)}')
else: 
    print(f'El usuario no es valido')