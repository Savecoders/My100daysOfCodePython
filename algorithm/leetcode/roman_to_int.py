#Roman numerals are represented by seven different symbols


ROMAN_SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

ROMAN_SYMBOLS_TWO_CHAR = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}


class Solution:
    def romanToInt(romano: str) -> int:
        counter = 0
        i = 0
        if len(romano) >= 1 and len(romano) <= 15:
            while i <= len(romano)-1:
                try:

                    #for the cases of IV IX XL .....
                    if((romano[i]+romano[i+1]) in ROMAN_SYMBOLS_TWO_CHAR):
                        counter += ROMAN_SYMBOLS_TWO_CHAR[(
                            romano[i]+romano[i+1])]
                        i += 2
                    else:
                        counter += ROMAN_SYMBOLS[romano[i]]
                        i += 1
                # error in romano[i+1]
                except:
                    counter += ROMAN_SYMBOLS[romano[i]]
                    i += 1
        return counter


print(Solution.romanToInt("MCMXCIV"))
