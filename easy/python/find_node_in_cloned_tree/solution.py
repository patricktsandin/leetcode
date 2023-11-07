"""
Given two binary trees original and cloned and given a reference to a node
target in the original tree.
The cloned tree is a copy of the original tree.
Return a reference to the same node in the cloned tree.
Note that you are not allowed to change any of the two trees or the target
node and the answer must be a reference to a node in the cloned tree.
"""


from unittest import TestCase
from collections import deque
from copy import copy


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """Solves iteratively in linear time and logarithmic space."""

    @staticmethod
    def get_target_copy(
        original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        """
        Given two trees and a target node from the first tree, find the
        corresponding node from the second tree.
        :param original: Original tree from which target node is derived
        :param cloned: Clone of original tree
        :param target: Node to seek out in cloned tree
        :return: Node from cloned tree matching target
        """
        value = target.val
        stack = [cloned]
        while stack:
            node = stack.pop()
            if node.val != value:
                children = list(filter(None, [node.left, node.right]))
                stack.extend(children)
            else:
                return node


class TestGetTargetCopy(TestCase):
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

    def create_trees(self, values):
        """Create pairs of trees for testing."""
        return (
            self.create_tree(copy(values)),
            self.create_tree(copy(values))
        )

    def test_minimum_input(self):
        values = deque([0])
        original, cloned = self.create_trees(values)

        expected = cloned
        result = Solution.get_target_copy(original, cloned, original)
        self.assertIs(expected, result)

    def test_typical_input_1(self):
        values = deque([7, 4, 3, None, None, 6, 19])
        original, cloned = self.create_trees(values)

        expected = cloned.right
        result = Solution.get_target_copy(original, cloned, original.right)
        self.assertIs(expected, result)

    def test_typical_input_2(self):
        values = deque([8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])
        original, cloned = self.create_trees(values)

        expected = cloned.right.right.right
        result = Solution.get_target_copy(
            original, cloned, original.right.right.right
        )
        self.assertIs(expected, result)

    def test_typical_input_3(self):
        values = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        original, cloned = self.create_trees(values)

        expected = cloned.left.right
        result = Solution.get_target_copy(
            original, cloned, original.left.right
        )
        self.assertIs(expected, result)
