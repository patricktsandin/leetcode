from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns tree values in the order they would be discovered by a
        depth-first search algorithm on the ascent from left to right.
        Recursive depth-first search algorithm in linear time and space.
        :param root: Root of a binary tree
        :return: An iterable of node values
        """
        # Work in progress
        pass
