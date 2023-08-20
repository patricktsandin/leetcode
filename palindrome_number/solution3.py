class Solution:
    """Checks if an integer is a palindrome in O(n) time and O(n) space."""
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
