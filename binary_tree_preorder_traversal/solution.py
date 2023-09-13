from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
        """
        Returns pre-order traversal of the values of a binary tree
        using an iterative DFS algorithm in linear space and time.
        Optimizing for readability.  Beats 85% of LeetCoders on runtime.
        :param root: Root of a binary tree to traverse
        :return: List of tree nodes
        """
        result = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                result.append(node.val)
                children = list(filter(None, [node.right, node.left]))
                stack.extend(children)
        return result
