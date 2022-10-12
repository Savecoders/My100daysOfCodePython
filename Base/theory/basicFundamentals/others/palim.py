
letter = input("Enter a letter: ")


def palimdromo(letter):
    letter = letter.lower().replace(" ", "")
    return letter == letter[::-1]


def run():

    print("Es palimdromo"
          if palimdromo(letter) else
          "No es palimdromo"
          )


if __name__ == '__main__':
    run()
