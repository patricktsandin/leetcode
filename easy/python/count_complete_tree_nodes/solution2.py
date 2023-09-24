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
        """Count nodes in a complete binary tree using a binary search
        algorithm in logarithmic time and space."""
        final_node = 1
        while root:
            if self.get_depth(root.right) == self.get_depth(root.left):
                root = root.right
                final_node = final_node * 2 + 1
            else:
                root = root.left
                final_node *= 2
        return final_node // 2
