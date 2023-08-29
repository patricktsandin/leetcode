class Solution:
    """Adds two string-formatted binary numbers and returns the same."""
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
