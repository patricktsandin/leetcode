# Given a string s, reverse only all the vowels in the string and return it.

class Solution:
    """Beats 89.07% of LeetCoders on compute."""
    @staticmethod
    def reverse_vowels(s: str) -> str:
        """Returns string with all vowels reversed in linear time and space
        using an iterative algorithm."""
        vowels = [vowel for vowel in s if vowel in 'aAeEiIoOuU']
        return ''.join([
            char if char not in 'aAeEiIoOuU'
            else vowels.pop()
            for char in s
        ])
