# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Beats 94.81% of LeetCoders on runtime and 60.91% on memory usage."""
    @staticmethod
    def reverse_integer_bits(integer: int) -> int:
        """Reverse the bits in an integer with iterative algorithm in
        logarithmic space and time."""
        reversed_integer = 0
        while integer:
            reversed_integer = reversed_integer * 2 + integer % 2
            integer //= 2
        return reversed_integer

    def get_depth(self, root: Optional[TreeNode], leaf_id=0) -> int:
        """Determine depth of specific leaf node (or max depth if none
        provided) using iterative algorithm to convert node id into
        tree traversal path in logarithmic time and space."""
        path = self.reverse_integer_bits(leaf_id) // 2
        depth = 0
        while root:
            if path % 2 == 0:
                root = root.left
            else:
                root = root.right
            depth += 1
            path //= 2
        return depth

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        """Count nodes in a complete binary tree using a binary search
        algorithm in logarithmic time and space."""
        if not root:
            return 0

        max_depth = self.get_depth(root)
        leaf1_id = 2**(max_depth - 1)
        leaf2_id = node_count = 2**max_depth - 1
        min_depth = self.get_depth(root, leaf2_id)

        if max_depth == min_depth:
            return node_count

        while abs(leaf1_id - leaf2_id) > 1:
            mid_leaf_id = (leaf1_id + leaf2_id) // 2
            mid_depth = self.get_depth(root, mid_leaf_id)
            if mid_depth == max_depth:
                leaf1_id = mid_leaf_id
            elif mid_depth == min_depth:
                leaf2_id = mid_leaf_id

        return leaf1_id
