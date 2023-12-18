class Solution:
    @staticmethod
    def hamming_weight(n: int) -> int:
        """
        Returns the Hamming Weight of an integer.
        :param n: Integer
        :return: Hamming weight
        """
        weight = 0
        while n:
            weight += n % 2
            n //= 2
        return weight
