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
        subtrees = [root]
        while subtrees:
            node = subtrees.pop()
            children = [child for child in (node.left, node.right) if child]
            if low <= node.val <= high:
                sum_ += node.val
                subtrees.extend(children)
            elif children:
                midrange = (low+high)/2
                min_distance = min(abs(child.val - midrange) for child in children)
                subtrees.extend(
                    child for child in children
                    if abs(child.val - midrange) == min_distance
                )
        return sum_


# noinspection DuplicatedCode
class TestRangeSumBST(TestCase):
    N = None

    PERFECT_TREE = (
                     50,
             25,             75,
         13,     38,     63,     88,
        7, 19, 32, 44, 57, 69, 82, 94
    )

    HOLLOW_TREE = (
                     50,
             25,             75,
         13,      N,      N,     88,
        7,  N,                  N, 94
    )

    DIAMOND_TREE = (
                     50,
             25,             75,
          N,     38,     63,      N,
                N, 44, 57
    )

    LINEAR_TREE = (
                     50,
              N,             75,
                          N,     88,
                                N, 94
    )

    ZIGZAG_TREE = (
                     50,
              N,             75,
                         63,      N,
                        N, 69
    )

    TREES = {
        "perfect": PERFECT_TREE,
        "hollow": HOLLOW_TREE,
        "diamond": DIAMOND_TREE,
        "linear": LINEAR_TREE,
        "zigzag": ZIGZAG_TREE
    }

    @staticmethod
    def create_tree(values: tuple) -> TreeNode:
        """Generate a tree given a deque of node values."""
        values = deque(values)

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

    def multi_tree_test(self, *, low, high, expected):
        for name, tree in self.TREES.items():
            with self.subTest(name):
                root = self.create_tree(tree)
                result = Solution.range_sum_bst(root, low, high)
                self.assertEqual(expected[name], result)

    def test_impossible_range(self):
        expected = {
            "perfect": 0,
            "hollow": 0,
            "diamond": 0,
            "linear": 0,
            "zigzag": 0
        }
        self.multi_tree_test(low=51, high=49, expected=expected)

    def test_out_of_bounds_range(self):
        expected = {
            "perfect": 0,
            "hollow": 0,
            "diamond": 0,
            "linear": 0,
            "zigzag": 0
        }
        self.multi_tree_test(low=101, high=999, expected=expected)

    def test_far_left_range(self):
        expected = {
            "perfect": 7,
            "hollow": 7,
            "diamond": 0,
            "linear": 0,
            "zigzag": 0
        }
        self.multi_tree_test(low=0, high=10, expected=expected)

    def test_far_right_range(self):
        expected = {
            "perfect": 264,
            "hollow": 182,
            "diamond": 0,
            "linear": 182,
            "zigzag": 0
        }
        self.multi_tree_test(low=80, high=100, expected=expected)

    def test_middle_range(self):
        expected = {
            "perfect": 151,
            "hollow": 50,
            "diamond": 151,
            "linear": 50,
            "zigzag": 50
        }
        self.multi_tree_test(low=44, high=57, expected=expected)

    def test_full_range(self):
        expected = {
            "perfect": 756,
            "hollow": 352,
            "diamond": 352,
            "linear": 307,
            "zigzag": 257
        }
        self.multi_tree_test(low=0, high=100, expected=expected)
