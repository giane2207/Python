lista_pares = []
lista_impares = []
for i in range(10):
    if (i % 2 == 0):
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(f'Lista de numeros pares: ')
for i in lista_pares:
    print(f'Numero: {i}')

print(f'Lista de numeros impares: ')
for i in lista_impares:
    print(f'Numero: {i}')