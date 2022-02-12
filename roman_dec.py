ROMAN_VAL = [
    ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
    ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
    ('IV', 4), ('I', 1)
]
"""MCMXLIX = 1949"""
def solution(roman):
    i = 0
    result = 0
    for rom, num in ROMAN_VAL:
        while roman[i : i + len(rom)] == rom:
            result += num
            i += len(rom)
    return result

