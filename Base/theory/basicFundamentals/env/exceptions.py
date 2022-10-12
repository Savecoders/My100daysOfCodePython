

def divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            raise ValueError("You must enter a positive number")
        print(divisors(n))
        print("End of program")
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    run()
