import json

def seeScores():
    with open('scores.json') as f:
        data = json.load(f)

    data["scores"].sort(key=lambda x: (x["difficulty"], x["score"]), reverse=True)

    i = 1
    for score in data["scores"]:
        print(i, "-", "Nombre: ", score['user'], "-", "Puntaje:", score['score'], "Dificultad: ", score["difficulty"])
        i +=1