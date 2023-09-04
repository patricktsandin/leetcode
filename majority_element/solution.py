from collections import Counter


class Solution:
    """Returns the majority element from an array in O(n) time
    and O(n) space."""
    def majorityElement(self, nums):
        return Counter(nums).most_common(1)[0][0]
