import random
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden
# que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el
# mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas

score = 0

#creo una lista de tuplas con 3 preguntas aleatorias, sus opciones y rtas
questions_to_ask = random.choices(list(zip(questions, 
answers, correct_answers_index)), k=3)
for qs, ans, cor_ans in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(qs)
    for i, answer in enumerate(ans):
        print(f"{i + 1}. {answer}")
     # El usuario tiene 2 intentos para responder
     # correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if(not user_answer.isdigit() or not (1 <= int(user_answer) <= 4)): 
            print("respuesta no válida")
            exit(1)
        user_answer = int(user_answer) - 1
        # Se verifica si la respuesta es correcta
        if user_answer == cor_ans:
            score+=1
            print("¡Correcto!")
            break
        score -= 0.5
    else:
        # Si el usuario no responde correctamente después de
        # 2 intentos, se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(ans[cor_ans])
    # Se imprime un blanco al final de la pregunta
    print()
print(f"Tu puntaje es de {score}")