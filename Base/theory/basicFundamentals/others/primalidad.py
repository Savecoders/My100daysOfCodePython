
# formula clasica
def primary(number):
    count = 0
    if number == 1:
        return True

    for i in range(2, number+1):
        if number % i == 0:
            count += 1

        if count > 2:
            break

    return count <= 2


def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)

# Teoria de wilson


def teoryWilson(number):
    return (factorial(number-1) + 1) % number == 0


def run():
    number = int(input("Enter a number: "))
    print("Es primo" if primary(number) else "No es primo")


if __name__ == '__main__':
    run()
