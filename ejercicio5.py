mi_lista = [0]*10
for i in range(10):
    num =  int(input("Ingrese un numero: "))
    mi_lista[i] = num

#i= 0
#while (i < 10 and mi_lista[i] > 0):
 #   print (f'Numero: {mi_lista[i]}')
 #   i += 1

for i in range(10):
    if (mi_lista[i] >= 0):
        print (f'Numero: {mi_lista[i]}')
    else: break
