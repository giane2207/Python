clients = [
" Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
" Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
"luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
" ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
"carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
"alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
"patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
"MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
"SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
"Damián Castillo ", None, "", " "
]

def eliminar_espacios (clients: list):
    """Elimina espacios extra en los nombres"""
    return [cliente.strip() for cliente in clients]

def convertir_a_titulo (clients: list):
    """Convierte los nombres de los clientes a formato titulo"""
    return [cliente.title() for cliente in clients]

def eliminar_duplicados(clients: list):
    """Elimina los clientes repetidos"""
    return list(set(clients))

def eliminar_nulos (clients: list):
    """Elimina los valores vacios o nulos"""
    return [cliente for cliente in clients if cliente and cliente.strip()]


# Ejecuto las funciones de limpieza 
clients = eliminar_nulos(clients)
clients = eliminar_espacios(clients)
clients = convertir_a_titulo(clients)
clients = eliminar_duplicados(clients)
clients.sort()

print(clients)