from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ascending = descending = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                descending = False
            elif nums[i] < nums[i - 1]:
                ascending = False
        return ascending or descending
