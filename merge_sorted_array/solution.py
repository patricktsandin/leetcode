class Solution:
    """Merges two sorted lists in-place in O(n * log n) time and O(1) space."""
    def merge(self, nums1, m, nums2, n):
        if n:
            del nums1[-n:]
        nums1.extend(nums2)
        nums1.sort()
