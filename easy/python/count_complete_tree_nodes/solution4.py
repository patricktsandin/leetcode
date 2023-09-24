# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def depth(self, node):
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        """Count nodes in a complete binary tree using a binary search
        algorithm in logarithmic time and space."""
        if not root:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if right_depth == left_depth:
            return self.count_nodes(root.right) + 2**left_depth
        else:
            return self.count_nodes(root.left) + 2**right_depth
