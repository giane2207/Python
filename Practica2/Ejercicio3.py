rules =  """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

# Genero una lista de reglas separadas por el argumento
rules = rules.split('.\n')

keyword = input('Ingrese una palabra clave: ')
rules_keyword = []

# Busco las reglas que contengan esa keyword y la guarda en nueva lista
for rule in rules:
    if (keyword in rule):
        rules_keyword.append(rule)

print(f'Reglas que contienen la palabra "{keyword}": ')
for rule in rules_keyword:
    print(f' - {rule}')