# Given the root of a binary tree, invert the tree, and return its root.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Beats 92.59% of LeetCoders on runtime."""
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Returns mirrored binary tree in linear time and logarithmic
        space using recursive algorithm."""
        if root:
            root.left = self.invert_tree(root.left)
            root.right = self.invert_tree(root.right)
            root.left, root.right = root.right, root.left
        return root
