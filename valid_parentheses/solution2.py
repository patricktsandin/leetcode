class Solution:
    """Checks whether or not a set of grouping symbols is appropriately
    matched in a given string in O(n) space and O(n) time"""

    def isValid(self, s):
        if len(s) % 2 != 0:
            return False

        closers_by_openers = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in closers_by_openers:
                stack.append(char)
            else:
                if not stack or not char == closers_by_openers[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return not stack
