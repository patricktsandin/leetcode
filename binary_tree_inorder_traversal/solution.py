class Solution:
    """Returns the left-to-right order of values in a binary tree without
    using recursion in O(n) time and O(n) space."""
    def inorderTraversal(self, root):
        stack = [root]
        result = []
        while stack and root:
            current = stack[-1]
            left = stack[-1].left
            right = stack[-1].right
            if left:
                stack.append(left)
                current.left = None
            else:
                result.append(current.val)
                stack.pop()
                if right:
                    stack.append(right)
        return result
