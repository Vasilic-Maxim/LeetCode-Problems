from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = prev = sum(nums[:k])
        for i in range(k, len(nums)):
            prev += -nums[i - k] + nums[i]
            result = max(result, prev)
        return result / k
