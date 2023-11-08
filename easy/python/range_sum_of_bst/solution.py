"""
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [
low, high].
"""


from typing import Optional
from unittest import TestCase
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
        pass


class TestRangeSumBST(TestCase):
    @staticmethod
    def create_tree(values: deque) -> TreeNode:
        """Generate a tree given a deque of node values."""

        root = TreeNode(values.popleft())
        parents = deque([root])
        while values:
            parent = parents.popleft()
            if left := values.popleft():
                parent.left = TreeNode(left)
                parents.append(parent.left)
            if values and (right := values.popleft()):
                parent.right = TreeNode(right)
                parents.append(parent.right)
        return root

    def test_minimum_input(self):
        pass
