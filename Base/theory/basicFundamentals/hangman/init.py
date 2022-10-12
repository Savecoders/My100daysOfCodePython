import random
import unicodedata
import os
from hangman import hangmanBank


def removeAceents(word) -> str:
    formatCode = unicodedata.normalize('NFKD', word)
    wordWithoutAccent = u"".join(
        [c for c in formatCode if not unicodedata.combining(c)])
    return wordWithoutAccent


def selectWord() -> str:

    with open("src/data.txt", "r", encoding="utf-8") as f:
        words = [line for line in f]

    word = words[random.randint(0, len(words) - 1)].strip()

    return removeAceents(word).capitalize()


def ocultWord(word) -> str:
    ocultWord = word[0] + ("_" * (len(word)-2)) + word[-1]
    return ocultWord


def isLetterInWord(letter, word) -> bool: return (letter in word)


def completedOcultWord(letter, word, ocultWord) -> str:
    ocultWordList = list(ocultWord)
    for i in range(len(word)):
        if letter == word[i]:
            ocultWordList[i] = letter

    return ''.join(ocultWordList)


def initialTable() -> None:
    print("Welcome to Hangman Game")
    print("You have to guess the word")
    print("You have 5 tries")
    print("Good luck")


def inputPlayer() -> str:

    letter = str(input("Enter a letter: "))
    return letter


def triesPLayer() -> None:
    tries = 0
    word = selectWord()
    incompleteWord = ocultWord(word)
    while tries < 5:
        print("The word is: ", incompleteWord)
        print(hangmanBank[tries]+"\n tries: "+str(tries)+" / 5\n")
        letter = inputPlayer()
        if(isLetterInWord(letter, word)):
            print("The letter is in the word")
            incompleteWord = completedOcultWord(letter, word, incompleteWord)
            if(incompleteWord == word):
                print("You win")
                break
        else:
            print("The letter is not in the word")
            tries += 1

        os.system("clear")
        if tries == 5:
            print("You lose")
            print(hangmanBank[tries]+"\n tries: "+str(tries)+" / 5\n")
            print("The word was: ", word)


def run():
    initialTable()
    triesPLayer()


if __name__ == '__main__':
    obj = {"name": "javier"}
    print(obj["edad"])
# run()
