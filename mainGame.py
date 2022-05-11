import json

def getInput(text, answers, printQuestion = True):
	if printQuestion:
		inputText = text 
	else: 
		inputText = ''
	response = input(inputText)
	if not response.isdigit() or int(response) > len(answers) or int(response) <= 0:
		print("Seleciona una opción valida")
		getInput(text, answers, printQuestion = False)
	return int(response)

def play(difficulty, playerName):
    print(f"El modo de juego es preguntas con dificultad {difficulty}")

    json_file = open('preguntas.json')
    questions_json = json.load(json_file)
    questions = questions_json.get('questions')
    responses = []

    print('Bienvenido al juego de la vida')
    input('Presione Enter para la siguiente pregunta')

    for question in questions:
        responses.append(askQuestion(question))
    correct_answers = len([response for response in responses if response])
    print(f'Juego terminado, respondiste: {correct_answers} respuestas correctamente')
    saveScore(playerName, correct_answers)

def askQuestion(question: dict):
	texto = question.get('question')
	inputText = f'¿{ texto }? \n'
	for index, answer in enumerate(question['answers']):
		inputText = inputText + (
			f'{index + 1}: '
			f'{answer} \n')
	inputResponse = getInput(inputText, question['answers'])
	return inputResponse == question["correct"]

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