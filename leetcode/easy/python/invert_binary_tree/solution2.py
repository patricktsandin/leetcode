# Given the root of a binary tree, invert the tree, and return its root.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Returns mirrored binary tree in linear time and logarithmic
        space using iterative DFS algorithm."""
        stack = [root]
        while stack and root:
            node = stack.pop()
            children = list(filter(None, [node.left, node.right]))
            node.left, node.right = node.right, node.left
            stack.extend(children)
        return root
