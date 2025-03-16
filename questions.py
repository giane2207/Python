import random
# Preguntas para el juego
questions = [ "¿Qué función se usa para obtener la longitud de una cadena en Python?", 
             "¿Cuál de las siguientes opciones es un número entero en Python?",
             "¿Cómo se solicita entrada del usuario en Python?",
            "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
            "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers =  [("size()", "len()", "length()", "count()"),
            ("3.14", "'42'", "10", "True"),
            ("input()", "scan()", "read()", "ask()"),
            ("// Esto es un comentario",
            "/* Esto es un comentario */", 
            "-- Esto es un comentario",
            "# Esto es un comentario",),
            ("=", "==", "!=", "===")]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Se seleccionan 3 preguntas sin repeticion
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

score = 0.0
# El usuario deberá contestar 3 preguntas 
# Se muestra la pregunta y las respuestas posibles
for question, options, correct_index in questions_to_ask:
     print (question)
     for i, option in enumerate(options):
         print(f'{i+1}. {option}') 

     # El usuario tiene 2 intentos para responder correctamente
     for intento in range(2):
         user_answer = input("Respuesta: ")
    
         # Se verifica que la respuesta sea un numero dentro del rango
         #if not user_answer.isnumeric() or user_answer.isnumeric() and int(user_answer)-1 not in range(len(options)):
         if not user_answer.isnumeric() or int(user_answer)-1 not in range(len(options)):
             print ("Respuesta no valida!")
             exit(1)

         user_answer = int(user_answer) - 1
         # Se verifica si la respuesta es correcta
         if user_answer == correct_index:
             print("¡Correcto!")
             score += 1
             break
         # Si el usuario no responde correctamente después de 2 intentos,
         # se muestra la respuesta correcta
         else:
             score -= 0.5
             if intento == 1:
                 print("Incorrecto. La respuesta correcta es:")
                 print(options[correct_index])

print(f'Fin del juego! El puntaje obtenido ha sido: {score}')