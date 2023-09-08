class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """Converts base 26 alphabetic string representation of integer
        to base 10 representation in linear time and space using iteration."""
        result = 0
        for index, char in enumerate(reversed(columnTitle)):
            result += (ord(char) - 64)*26**index
        return result
