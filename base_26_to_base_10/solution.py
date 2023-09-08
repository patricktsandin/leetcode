class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """Converts base base 10 integer to base 26 alphabetic string
        representation of integer in linear time and space using iteration."""
        # Work in progress
        result = []
        power = 0
        while True:
            base10_digit = (columnNumber % 26**(power + 1)) // 26**power
            if base10_digit:
                result.insert(0, chr(base10_digit + 64))
                power += 1
            else:
                break
        return ''.join(result)
