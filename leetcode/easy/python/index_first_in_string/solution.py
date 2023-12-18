class Solution:
    """Get first index of substring needle in string haystack in O(1)
    space and O(n) time."""
    def strStr(self, haystack, needle):
        return haystack.find(needle)
