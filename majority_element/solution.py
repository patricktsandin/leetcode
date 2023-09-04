from collections import Counter


class Solution:
    """Returns the majority element from an array in O(n) time
    and O(1) space."""
    def majorityElement(self, nums):
        return Counter(nums).most_common(1)[0][0]
