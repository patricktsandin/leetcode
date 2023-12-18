# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.

from typing import List


class Solution:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        """Returns intersection of two arrays."""
        nums1.sort()
        nums2.sort()
        for nums in [nums1, nums2]:
            last_element = len(nums) - 1
            index = 0
            while index < last_element:
                if nums[index] == nums[index + 1]:
                    del nums[index]
                    last_element -= 1
                else:
                    index += 1
        length1 = len(nums1)
        index1 = 0
        length2 = len(nums2)
        index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] > nums2[index2]:
                del nums2[index2]
                length2 -= 1
            elif nums2[index2] > nums1[index1]:
                del nums1[index1]
                length1 -= 1
            else:
                index1 += 1
                index2 += 1
        if length1 > length2:
            return nums2
        else:
            return nums1
