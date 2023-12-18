class Solution:
    """Get length of last space-delimited element from string in
    O(n) time and space."""
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])
