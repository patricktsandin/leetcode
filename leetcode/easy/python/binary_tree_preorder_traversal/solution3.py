from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns pre-order traversal of the values of a binary tree
        using a recursive algorithm in constant space and time.
        :param root: Root of a binary tree to traverse
        :return: Returns a list of tree values
        """
        return [
            root.val,
            *self.preorder_traversal(root.left),
            *self.preorder_traversal(root.right)
        ] if root else []
