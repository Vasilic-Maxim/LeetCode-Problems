from typing import *


class Solution:
    """
    Time: O(n * log_n) - for sorting
    Space: O(n) - sorted list
    """

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        p1 = p2 = 0
        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                p1 = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != nums_sorted[j]:
                p2 = j
                break

        return p2 - p1 + 1
