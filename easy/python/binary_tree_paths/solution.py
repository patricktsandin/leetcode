# Given the root of a binary tree, return all root-to-leaf paths in any order.

from typing import Iterator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def binary_tree_paths(root: TreeNode) -> Iterator[str]:
        """Return all root-to-leaf paths in a binary tree using an iterative
        depth-first search algorithm in logarithmic space and linear time."""
        stack = [(root, (str(root.val),))]
        while stack:
            node, path = stack.pop()
            children = list(filter(None, [node.left, node.right]))
            for child in children:
                stack.append((child, path + (str(child.val),)))
            if not children:
                yield '->'.join(path)
