class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root):
        """Return whether child trees are height-balanced and maximum depth
        in O(n) time and O(log n) space."""
        if not root:
            return True, 0
        left_balanced, left_depth = self.is_balanced(root.left)
        right_balanced, right_depth = self.is_balanced(root.right)
        children_balanced = left_balanced and right_balanced
        self_balanced = abs(left_depth - right_depth) <= 1
        return (
            children_balanced and self_balanced,
            max(left_depth, right_depth) + 1
        )

    def isBalanced(self, root):
        """Return whether binary tree is height-balanced."""
        return self.is_balanced(root)[0]
