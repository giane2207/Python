import csv 

path_individuos = '../files/usu_individual_T324.txt'
path_hogar = '../files/usu_hogar_T324.txt'


with open(path_individuos) as csv_individuos:
    SEXO = 'CH04'
    PONDERA = 'PONDERA'
    EDAD = 'CH06'
    SECUNDARIO = 'NIVEL_ED'

    cantMujeres = 0
    cantVarones = 0
    cantSecundario = 0

    reader = csv.DictReader(csv_individuos, delimiter= ';')
    
    for row in reader:
        if row[SEXO] == '1':
            cantVarones = cantVarones + int(row[PONDERA])
        else:
            cantMujeres = cantMujeres + int(row[PONDERA])
        if row[EDAD] >= '18' and row[SECUNDARIO] == '4' :
            cantSecundario = cantSecundario + int(row[PONDERA])

print (f'Total mujeres: {cantMujeres}')
print (f'Total varones: {cantVarones}')
print (f'Total de personas mayores de edad que han completado los estudios secundarios: {cantSecundario}')


with open(path_hogar) as csv_hogar:
    PROPIETARIO = 'II7'
    PONDERA_H = 'PONDERA'
    MIEMBROS = 'IX_TOT'
    BANO = 'IV8'
    AGLOMERADO = 'AGLOMERADO'

    cantPropietarios = 0
    totalHogares = 0

    aglomerados = {}

    reader = csv.DictReader(csv_hogar, delimiter=';')

    for row in reader:

        totalHogares = totalHogares + int(row[PONDERA_H])
        if (row[PROPIETARIO] == '1'):
            cantPropietarios = cantPropietarios + int(row[PONDERA_H])

        # Se procesan los aglomerados con mas de dos ocupantes
        if (row[MIEMBROS] > '2'):
            aglo = row[AGLOMERADO] # Se guarda el codigo de aglomerado
            tieneBanio = row[BANO] # Se guarda 1 o 2

            # Agrego el aglomerado sino existe e inicializo su diccionario
            if aglo not in aglomerados:
                aglomerados[aglo] = {'1':0, '2': 0} 
            
            # Incremento en el aglomerado la cantidad de viviendas que poseen o no baño
            aglomerados[aglo][tieneBanio] += int(row[PONDERA_H])

## Busco min y max aglomerado de acuerdo a la cantidad de viviendas sin baño
codMaxAglomerado = max(aglomerados, key=lambda k: aglomerados[k]['2'])
codMinAglomerado = min(aglomerados, key=lambda k: aglomerados[k]['2'])

aglomeradosNombres = {
                    '2': 'Gran La Plata', '3': 'Bahia Blanca - Cerri', '4': 'Gran Rosario',
                    '5': 'Gran Santa Fe', '6': 'Gran Parana', '7': 'Posadas', '8': 'Gran Resistencia',
                    '9': 'Comodoro Rivadavia - Rada Tilly', '10': 'Gran Mendoza', '12': 'Corrientes',
                    '13': 'Gran Cordoba', '14': 'Concordia', '15': 'Formosa', '17': 'Neuquen - Plottier',
                    '18': 'Santiago del Estero - La Banda', '19': 'Jujuy - Palpala', '20': 'Rio Gallegos',
                    '22': 'Gran Catamarca', '23': 'Gran Salta', '25': 'La Rioja', '26': 'Gran San Luis',
                    '27': 'Gran San Juan', '29': 'Gran Tucuman - Tafi Viejo', '30': 'Santa Rosa - Toay',
                    '31': 'Ushuaia - Rio Grande', '32': 'Ciudad Autonoma de Buenos Aires',
                    '33': 'Partidos del GBA', '34': 'Mar del Plata', '36': 'Rio Cuarto',
                    '38': 'San Nicolas - Villa Constitucion', '91': 'Rawson - Trelew',
                    '93': 'Viedma - Carmen de Patagones'
}

procentajePropietarios = (totalHogares / cantPropietarios) * 100

print(f'El porcentaje de viviendas que son ocupadas por el/la propietario/a de la vivienda y del terreno son: {procentajePropietarios}')
print(f'el aglomerado con mayor cantidad de viviendas con más de 2 ocupantes que no posean baño: {aglomeradosNombres[codMaxAglomerado]}')
print(f'el aglomerado con menor cantidad de viviendas con más de 2 ocupantes que no posean baño: {aglomeradosNombres[codMinAglomerado]}')

