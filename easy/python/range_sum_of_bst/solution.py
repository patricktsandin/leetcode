"""
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [
low, high].
"""


from unittest import TestCase
from collections import deque


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solves iteratively in linear time and logarithmic space."""

    @staticmethod
    def range_sum_bst(root: TreeNode, low: int, high: int) -> int:
        """
        Returns the sum of a binary tree's values between a given range
        :param root: Root of the binary tree to search
        :param low: low value of search range, inclusive
        :param high: high value of search range, inclusive
        :return: sum of node values
        """
        sum_ = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                sum_ += node.val
            stack.extend(list(filter(None, [node.left, node.right])))
        return sum_


# noinspection DuplicatedCode
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

    def test_typical_input_1(self):
        root = self.create_tree(deque([10, 5, 15, 3, 7, None, 18]))
        low = 7
        high = 15
        expected = 32
        result = Solution.range_sum_bst(root, low, high)
        self.assertEqual(expected, result)

    def test_typical_input_2(self):
        root = self.create_tree(deque([10, 5, 15, 3, 7, 13, 18, 1, None, 6]))
        low = 6
        high = 10
        expected = 23
        result = Solution.range_sum_bst(root, low, high)
        self.assertEqual(expected, result)

    def test_typical_input_3(self):
        root = self.create_tree(deque([1, None, 2, None, 3, None, 4]))
        low = 1
        high = 3
        expected = 6
        result = Solution.range_sum_bst(root, low, high)
        self.assertEqual(expected, result)

    def test_typical_input_4(self):
        root = self.create_tree(deque([99, 88, 77, 1, 3, 6, None, 1, 5, 6]))
        low = 50
        high = 70
        expected = 0
        result = Solution.range_sum_bst(root, low, high)
        self.assertEqual(expected, result)
