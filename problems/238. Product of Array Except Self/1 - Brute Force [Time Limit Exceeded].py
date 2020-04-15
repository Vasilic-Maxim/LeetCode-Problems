from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(n)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums)):
            for j, num in enumerate(nums):
                if j != i:
                    result[i] *= num
        return result
