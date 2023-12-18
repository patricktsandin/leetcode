# Given the root of a binary tree, return all root-to-leaf paths in any order.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        """Return all root-to-leaf paths in a binary tree using a recursive
        depth-first search algorithm in linear space and time."""
        if not root:
            return []

        value = str(root.val)
        paths = []
        children = list(filter(None, [root.left, root.right]))
        for child in children:
            paths.extend(self.binary_tree_paths(child))
        for index, path in enumerate(paths):
            paths[index] = f"{value}->{path}"
        if not paths:
            paths.append(value)
        return paths
