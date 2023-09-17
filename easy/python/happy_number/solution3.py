from typing import Iterator


class Solution:
    @staticmethod
    def places(n) -> Iterator[int]:
        """
        Yields digit positions given integer in constant time and space
        :param n: Integer
        :return: Positions of input integer digits
        """
        place = 0
        while n:
            yield place
            n //= 10
            place += 1
        yield place

    def squares(self, n) -> Iterator[int]:
        """
        Yields a squared number in constant time and space
        :param n: Number to square
        :return: Squares of input integer digits
        """
        for _ in self.places(n):
            yield (n % 10)**2
            n //= 10

    def is_happy(self, n: int) -> bool:
        """
        Return whether a number is happy in linear time and space
        :param n: Potential happy number
        :return: Whether it is happy
        """
        all_n = set()
        while n != 1:
            n = sum(self.squares(n))
            if n in all_n:
                break
            else:
                all_n.add(n)
        return n == 1
