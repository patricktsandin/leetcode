class Solution:
    @staticmethod
    def hamming_weight(n: int) -> int:
        """
        Returns the Hamming Weight of an integer.
        :param n: Integer
        :return: Hamming weight
        """
        return n.bit_count()
