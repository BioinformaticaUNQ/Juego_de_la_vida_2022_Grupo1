import json
import os
import random

def clearConsole():
    if os.name == 'nt':
        clear = lambda: os.system('cls')
    else:
        clear = lambda: os.system('clear')
    clear()

def getQuestions():
	jsonFile = open('questions.json')
	questionsJson = json.load(jsonFile)
	questions = questionsJson.get('questions')
	random.shuffle(questions)
	questions.sort(key=getDifficulty)
	return questions

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
	return int(response)

def endGame(responses, gameOver, difficulty):
	if not gameOver:
		print("Felicidades, terminaste el juego!")
	qtyCorrectAnswers = len([response for response in responses if response])
	print(f'Juego terminado, respondiste: {qtyCorrectAnswers} respuestas correctamente')
	playerName = input('Ingresa tu nombre para guardar tu puntaje:')
	saveScore(playerName, qtyCorrectAnswers, difficulty)

def play(difficulty):
    clearConsole()
    print('Bienvenido al juego de la vida')
    print(f"La dificultad del juego será {difficulty}, ¿estás liste?")

    questions = getQuestions()
    responses = []
    gameOver = False

    input('Presione Enter para comenzar')

    clearConsole()

    for question in questions:
    	response = askQuestion(question)
    	feedback(question, response)
    	shouldContinue = globals()[f"difficulty{difficulty}"](response, responses, questions)
    	if not shouldContinue:
    		gameOver = True
    		print("Perdiste :(")
    		break
    	responses.append(response)
    	clearConsole()
    endGame(responses, gameOver, difficulty)

def feedback(question, response):
	if response:
		print("!Respondiste correctamente!")
	else:
		print("Tu respuesta fue incorrecta")
		print("La respuesta correcta era:", question["answers"][question["correct"]-1])
	input('Presione enter para continuar')

def askQuestion(question: dict):
	texto = question.get('question')
	inputText = f'¿{ texto }? \n'
	for index, answer in enumerate(question['answers']):
		inputText = inputText + (
			f'{index + 1}: '
			f'{answer} \n')
	inputResponse = getInput(inputText, question['answers'])
	return inputResponse == question["correct"]

def saveScore(user, score, difficulty):
    with open('scores.json','r+') as file:
        fileData = json.load(file)
        newData = {
            "user": user,
            "score": score,
            "difficulty": difficulty
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
	return qtyWrongAnswers < (len(questions)/2)

def difficulty3(response, previousResponses, questions):
	return response