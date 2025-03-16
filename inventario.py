inventario = dict()
operaciones = ['Agregar producto',
               'Eliminar producto',
               'Mostrar inventario',
               'Salir']


fin_programa = False


while not fin_programa:
     # Se muestra el listado de operaciones
     print('Indique el numero de la operacion que desea realizar')
     for i, operacion in enumerate(operaciones):
         print(f'{i+1}. {operacion}')

     user_answer = int(input())
     match user_answer:
         case 1:
             nombre_producto = input('Ingrese nombre del producto: ')
             cant = int(input('Ingrese cantidad del producto: '))
             if nombre_producto in inventario:
                 inventario[nombre_producto] += cant
             else:
                 inventario[nombre_producto] = cant
         case 2: 
             nombre_producto = input('Ingrese nombre del producto que desea eliminar: ')
             if nombre_producto in inventario:
                 del(inventario[nombre_producto])
                 print(f'El pruducto {nombre_producto} se ha eliminado correctamente!')
             else: 
                 print(f'El producto {nombre_producto} no existe en el inventario')
         case 3: 
             for producto in inventario:
                 print(f'{producto}  ->  {inventario[producto]}')
         case 4: 
             fin_programa = True
         case _:
             print ('Respuesta no valida')
             fin_programa = True
