from bisect import bisect_left
from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """

    def checkIfExist(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1] == 0:
                return True
            else:
                mul = nums[i] * 2
                index = bisect_left(nums, mul)
                if nums[index] == mul:
                    return True
        return False

