ROMAN_SYMBOLS = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
    4000: "MN"
}

keys = list(ROMAN_SYMBOLS.keys())


class Solution:
    def intToRoman(num: int) -> str:
        if num >= 1 and num <= 3999:
            if num in ROMAN_SYMBOLS:
                return ROMAN_SYMBOLS[num]
            else:
                for i in range(len(keys) - 1):
                    if keys[i] < num and num < keys[i + 1]:
                        return ROMAN_SYMBOLS[keys[i]] + Solution.intToRoman(num - keys[i])
        else:
            return ""


print(Solution.intToRoman(1994))