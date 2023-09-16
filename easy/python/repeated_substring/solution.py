from collections import Counter


class Solution:
    def repeatedSubstringPattern(self, s):
        """Returns whether a string is composed of repeated substrings
        in O(n) space and O(n) time."""
        if len(s) == 1:
            return False

        primes = [
            241, 239, 233, 229, 227, 223, 211, 199, 197, 193, 191, 181, 179,
            173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109, 107,
            103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37,
            31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2
        ]
        counts = Counter(s)
        length = len(s)
        factors = [length] + [
            prime for prime in primes
            if all([
                factor % prime == 0
                for factor in [*counts.values(), length]
            ])
        ]

        for factor in factors:
            if s[:length // factor] * factor == s:
                return True
        return False