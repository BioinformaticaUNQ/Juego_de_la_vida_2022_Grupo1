import json

def seeScores():
    with open('scores.json') as f:
        data = json.load(f)

    data["scores"].sort(key=lambda x: x["score"], reverse=True)

    i = 1
    for score in data["scores"]:
        print(i, "-", score['user'], "-", score['score'])
        i +=1