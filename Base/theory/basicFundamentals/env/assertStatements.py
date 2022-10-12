

# Assert statements are used to check if a condition is true or false.

def palindrome(word):
    assert len(word) > 0, "Please enter a word."
    return word == word[::-1]


def defineNumber(num):
    assert num > 0, "Please enter a positive number."
    if num % 2 == 0:
        return "Even number."
    else:
        return "Odd number."


def run():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(arr[11])


if __name__ == "__main__":
    run()
