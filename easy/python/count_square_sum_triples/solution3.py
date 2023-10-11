from math import sqrt, gcd


class Solution:
    @staticmethod
    def countTriples(n: int) -> int:
        triples_count = 0
        for i in range(2, int(sqrt(n)) + 1):
            for j in range(1, i):
                if gcd(i, j) == 1 and (i - j) % 2 and (i*i + j*j) <= n:
                    triples_count += n//(i*i + j*j)
        return 2*triples_count


print(Solution.countTriples(5))