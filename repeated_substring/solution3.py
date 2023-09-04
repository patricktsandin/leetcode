class Solution:
    """Returns whether a string is composed of repeated substrings in
    O(n) space and O(n) time."""
    def repeatedSubstringPattern(self, s):
        return s in (s + s)[1:-1]
