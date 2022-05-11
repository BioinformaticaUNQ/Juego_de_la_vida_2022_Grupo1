import argparse
import mainGame
import scores

parser = argparse.ArgumentParser(description='Este es el juego de la vida, para ganar deberás responder correctamente las preguntas dadas según la dificultad elegida.')
parser.add_argument('-d', '--difficulty',
                    type=int,
                    help="""Dificultad del juego:
                             1 = fácil (Podés responder mal cualquier pregunta), 
                             2 = media (Podés responder mal hasta la mitad de las preguntas), 
                             3 = difícil (No podes responder mal ninguna pregunta)""",
                    required=True)
parser.add_argument('-m', '--mode',
                    type=int,
                    help="""Modo del juego:
                             1 = juego(Para responder las preguntas), 
                             2 = puntuación (Para ver las puntuaciones del juego)""",
                    required=True)
parser.add_argument('-u', '--user',
                    type=str,
                    help="""Indica el nombre del jugador""",
                    required=True)

args = parser.parse_args()

if args.mode == 1:
    mainGame.play(args.difficulty, args.user)
else:
    scores.seeScores()
    