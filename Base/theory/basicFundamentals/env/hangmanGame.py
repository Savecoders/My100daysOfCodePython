
import random


def letterSelect() -> str:
    letterOfGame = ["candado", "piedra", "tijeras", "regla", "ahorcado"]

    letterSelect = letterOfGame[random.randint(0, len(letterOfGame) - 1)]

    return letterSelect


def hangmanGame():
    Tries = 0
