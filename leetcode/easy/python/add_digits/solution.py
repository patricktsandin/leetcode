# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    @staticmethod
    def add_digits(number: int) -> int:
        """Adds the digits of provided number and all results
        until answer is a single digit."""
        while number > 9:
            intermediate = 0
            while number > 0:
                intermediate += number % 10
                number //= 10
            number = intermediate
        return number
