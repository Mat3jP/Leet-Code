class Solution:
    #def romanToInt(self, s: str) -> int:
    def romanToInt(self, s):
        values = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
        roman_string = s.upper()
        int_val = 0
        prev = None

        for letter in roman_string:
            if prev is not None and values[prev] < values[letter]:
                int_val += (values[letter] - 2*values[prev])
                print (f"\nfor letter {letter}, entered if\ncurrent:{letter}\nprev:{prev}")
                print (f"current int: {int_val}")
                continue
            else:
                print (f"\nfor letter {letter}, entered else\ncurrent:{letter}\nprev:{prev}")
                int_val += values[letter]
                print (f"current int: {int_val}")

            prev = letter

        return int_val