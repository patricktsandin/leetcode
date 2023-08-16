class Solution:
    def romanToInt(self, s: str) -> int:
        """Converts a roman numeral to an integer."""
        integer_by_numeral = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        integers = []
        for numeral in reversed(s):
            integer = integer_by_numeral[numeral]
            if integers and integer < abs(integers[-1]):
                integers.append(-integer)
            else:
                integers.append(integer)
        return sum(integers)
