class Solution:
    @staticmethod
    def reverse_bits(n: int) -> int:
        """
        Reverses an integer's bit order in constant time and space.
        Optimized for time, space, and concision.  Beats 99.40%
        of LeetCoders on runtime and 98.74% on memory.
        :param n: Integer
        :return: Binary-reversed integer
        """
        reversed_n = 0
        for _ in range(32):
            reversed_n = reversed_n * 2 + n % 2
            n //= 2
        return reversed_n
