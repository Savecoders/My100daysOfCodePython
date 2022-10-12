

import numbers


def read():
    numbers = []
    with open('file.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))


def write():
    names = ["Facundo", "Miguel", "Pepe", "Eduardo", "Jorge", "Rodrigo"]
    with open('names.txt', 'w') as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == "__main__":
    run()
