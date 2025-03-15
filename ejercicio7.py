mi_lista = []
for i in range(5):
    num = int(input("Ingrese un numero: "))
    mi_lista.append(num)

cadena = ''
for i in range(5):
    if (mi_lista[i] % 3 != 0):
         num = str(mi_lista[i])
         cadena = cadena + num + ' - '

print(cadena)