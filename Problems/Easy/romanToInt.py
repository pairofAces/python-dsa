# roman to int Leetcode

def romanToInt(s : str):
    # create a dictionary for the roman numerals and the values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    