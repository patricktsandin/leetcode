# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
from typing import Optional
from functools import cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def get_depth(self, root: Optional[TreeNode]) -> int:
        """Determine the left-side depth from a given node."""
        return 1 + self.get_depth(root.left) if root else 0

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        """Count nodes in a complete binary tree using a recursive binary
        search algorithm in logarithmic time and space."""
        if root:
            right_depth = self.get_depth(root.right)
            left_depth = self.get_depth(root.left)
            if right_depth == left_depth:
                left_nodes = 2**left_depth
                return self.count_nodes(root.right) + left_nodes
            else:
                right_nodes = 2**right_depth
                return self.count_nodes(root.left) + right_nodes
        else:
            return 0
