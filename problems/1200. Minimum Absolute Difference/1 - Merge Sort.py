from typing import *


class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        min_diff = float('inf')

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff < min_diff:
                min_diff = diff
                result = [[nums[i-1], nums[i]]]
            elif diff == min_diff:
                result.append([nums[i-1], nums[i]])
        return result
