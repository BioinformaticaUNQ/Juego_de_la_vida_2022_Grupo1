import json

def play(difficulty):
    print(f"El modo de juego es preguntas con dificultad {difficulty}")

	json_file = open('preguntas.json')

	preguntas_json = json.load(json_file)

	print(preguntas_json)

	print('Bienvenido al juego de la vid4')
	print('Presione Enter para la siguiente pregunta')

	for pregunta in preguntas_json:
		hacerPregunta(pregunta)

def askQuestion(pregunta: dict):
	print(pregunta)
	input_text = (
		f'¿'
	)
	input(fz)
	return 

def saveScore(user, score):
    with open('scores.json','r+') as file:
        file_data = json.load(file)
        new_data = {
            "user": user,
            "score": score
        }
        file_data["scores"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)