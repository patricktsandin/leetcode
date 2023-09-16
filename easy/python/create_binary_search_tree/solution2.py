class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        """Return the root of a height-balanced binary search tree in O(n)
        time and O(n * log n) space given a sorted array of integers."""
        return TreeNode(
            val=nums[len(nums)//2],
            left=self.sortedArrayToBST(nums[:len(nums)//2]),
            right=self.sortedArrayToBST(nums[len(nums)//2 + 1:])
        ) if nums else None
