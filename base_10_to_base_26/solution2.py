class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """Converts base base 10 integer to base 26 alphabetic string
        representation of integer in using iteration in logarithmic
        time and space"""
        result = []
        while columnNumber:
            columnNumber -= 1
            result.insert(0, chr(columnNumber % 26 + 65))
            columnNumber //= 26
        return ''.join(result)
