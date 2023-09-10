from math import log

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """Converts base base 10 integer to base 26 alphabetic string
        representation of integer in linear time and space using iteration
        in O(log n) time and space"""
        result = []
        borrow = 0
        # Find the resultant number's length in digits with a base-26 logarithm
        length = int(log(columnNumber, 26)) + 1
        position = 1
        # For each digit of the resultant number...
        while position <= length:
            # Get the base10 representation of the result digit
            base10_digit = (
                # Chop off greater digits with modulo
                (columnNumber % 26**position)
                # Chop off lesser digits with floor division
                // 26**(position - 1)
            ) + borrow
            # If the digit is less than A...
            if base10_digit < 1 and position < length:
                # Roll over to Z by adding 26
                result.insert(0, chr(base10_digit + 26 + 64))
                # Make sure we're borrowing from the next greatest digit
                borrow = -1
            elif base10_digit >= 1:
                result.insert(0, chr(base10_digit + 64))
                borrow = 0
            position += 1
        return ''.join(result)
