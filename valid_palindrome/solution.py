class Solution:
    """Checks if a phrase is a palindrome in O(n) time and O(n) space"""
    def isPalindrome(self, s):
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]
