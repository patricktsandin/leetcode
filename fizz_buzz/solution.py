class Solution:
    """Solves fizzbuzz in O(n) time and space complexity."""
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for integer in range(1, n + 1):
            if integer % 3 == 0 and integer % 5 == 0:
                result.append("FizzBuzz")
            elif integer % 3 == 0:
                result.append("Fizz")
            elif integer % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(integer))
        return result
