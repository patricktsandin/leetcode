from collections import Counter


class Solution:
    """Return whether s and t are anagrams in O(n) and O(n) space."""
    def isAnagram(self, s, t):
        return Counter(t) == Counter(s)
