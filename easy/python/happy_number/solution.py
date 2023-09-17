class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Return whether a number is happy using iterative algorithm.
        :param n: Potential happy number
        :return: Whether it is happy
        """
        all_n = set()
        while n is not 1:
            n = sum([int(digit)**2 for digit in str(n)])
            if n in all_n:
                break
            else:
                all_n.add(n)
        return n is 1
