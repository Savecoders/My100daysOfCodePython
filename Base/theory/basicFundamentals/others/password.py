import random


def generatePassword():
    password = ""
    for i in range(12):
        # codigo ascii de los caracteres
        password += chr(random.randint(65, 122))
    return password


def run():
    password = generatePassword()
    print("Tu nueva contraseña es: " + password)
    print("AEIOU"[0:4:2])


if __name__ == '__main__':
    run()
