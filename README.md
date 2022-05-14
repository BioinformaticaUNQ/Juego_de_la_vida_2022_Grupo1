# JuegoDeLaVida

Este juego de la vida es un juego de preguntas sobre Biología, este juego consta con 2 modalidades:

* [Ver scores](#como-ver-scores)
* [Jugar](#como-jugar)

## Prerrequisitos

Para poder jugar el juego los requisitos son los siguientes:

* Tener Python instalado

## Niveles de dificultad:

El juego tiene 3 niveles de dificultad

### Dificultad 1
Podés responder mal cualquier pregunta

### Dificultad 2
Podés responder mal hasta la mitad de las preguntas

### Dificultad 3
No podes responder mal ninguna pregunta

## Como ver scores

1. Clonar el proyecto
2. Con la consola hacer un cd hasta el path donde esta el proyecto clonado
3. Correr el siguiente comando: ``` python juegovida.py -d 1 -m 2 -u userName```

![image](https://user-images.githubusercontent.com/13736226/167754318-e3b071a0-0627-47c4-802e-18860d1fae37.png)

## Como jugar


1. Clonar el proyecto
2. Con la consola hacer un cd hasta el path donde esta el proyecto clonado
3. Correr el siguiente comando: ``` python juegovida.py -m MODO(1 o 2, para jugar o ver puntuación) -d DIFICULTAD(1,2 o 3)

![image](https://user-images.githubusercontent.com/13736226/167754707-061a7c9e-f4c9-4fd9-95ae-2c651f520d09.png)


## Como agregar preguntas

Para agregar preguntas solo se necesita ingresar al archivo [questions.json](https://github.com/BioInfUnq-grupo1/JuegoDeLaVida/blob/main/questions.json) y modificar el array de questions agregandole uno o mas objetos, el objeto question deberá tener la siguiente estructura:

 ```JSON
{
  "question":"En 1969, Robert Whittaker clasifico a los seres vivos en:",
  "answers":["2 reinos","5 reinos","4 reinos","9 reinos"],
  "correct":2,
  "difficulty":1
}
 ```
 
 En el campo question va la pregunta, en el campo answers es un array de strings con las opciones, podes poner la cantidad de opciones que quieras, en el campo correct indicas que opcion es la correcta en un integer y en difficulty la dificultad de la pregunta, esta última tambien es un integer
