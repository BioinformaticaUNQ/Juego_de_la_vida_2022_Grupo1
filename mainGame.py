import json

def getDifficulty(question):
	return question.get("difficulty")

def getInput(text, answers, printQuestion = True):
	if printQuestion:
		inputText = text 
	else: 
		inputText = ''
	response = input(inputText)
	if not response.isdigit() or int(response) > len(answers) or int(response) <= 0:
		print("Seleciona una opción valida")
		getInput(text, answers, printQuestion = False)
	return int(response) - 1

def play(difficulty, playerName):
    print(f"El modo de juego es preguntas con dificultad {difficulty}")

    jsonFile = open('questions.json')
    questionsJson = json.load(jsonFile)
    questions = questionsJson.get('questions')
    questions.sort(key=getDifficulty)
    responses = []
    gameOver = False

    print('Bienvenido al juego de la vida')
    input('Presione Enter para la siguiente pregunta')

    for question in questions:
    	response = askQuestion(question)
    	shouldContinue = globals()[f"difficulty{difficulty}"](response, responses, questions)
    	if not shouldContinue:
    		gameOver = True
    		print("Perdiste :(")
    		break
    	responses.append(response)

    if not gameOver:
    	print("Felicidades, terminaste el juego!")
    qtyCorrectAnswers = len([response for response in responses if response])
    print(f'Juego terminado, respondiste: {qtyCorrectAnswers} respuestas correctamente')
    saveScore(playerName, qtyCorrectAnswers)

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
        fileData = json.load(file)
        newData = {
            "user": user,
            "score": score
        }
        fileData["scores"].append(newData)
        file.seek(0)
        json.dump(fileData, file, indent = 4)

def difficulty1(response, previousResponses, questions):
	return True

def difficulty2(response, previousResponses, questions):
	responses = previousResponses.copy()
	responses.append(response)
	qtyWrongAnswers = len([response for response in responses if not response])
	print(qtyWrongAnswers)
	return qtyWrongAnswers < (len(questions)/2)

def difficulty3(response, previousResponses, questions):
	return response