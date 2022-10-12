

import math


def run():
    # print([i for i in range(0, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0])
    print({i: round(math.sqrt(i), 2) for i in range(0, 1000)})


def palimdrome(string): return string == string[::-1]


if __name__ == "__main__":
    run()
