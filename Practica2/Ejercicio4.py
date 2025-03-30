import string

def es_valido (user: str):
    return  (len(user) >= 5 and                 # Si contiene al menos 5 caracteres
            user.isalnum() and                  # Si contiene numeros y letras
            any(c.isdigit() for c in user) and  # Si contiene al menos un numero
            any(c.isupper() for c in user))     # Si contiene al menos una mayuscula

user = input('Ingrese nombre de usuario: ')
if (es_valido(user)):
    print(f'El usuario {user} es valido!!')
else: print(f'El usuario {user} no es valido :(')