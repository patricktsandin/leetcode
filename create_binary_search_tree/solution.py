class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        """Return the root of a height-balanced binary search tree in O(n)
        time and O(n * log n) space given a sorted array of integers."""
        root = TreeNode()
        stack = [(root, nums)]
        while stack:
            node, sublist = stack.pop()
            middle_index = len(sublist)//2
            left_sublist = sublist[:middle_index]
            right_sublist = sublist[middle_index + 1:]
            node.val = sublist[middle_index]
            if left_sublist:
                node.left = TreeNode()
                stack.append((node.left, left_sublist))
            if right_sublist:
                node.right = TreeNode()
                stack.append((node.right, right_sublist))
        return root
