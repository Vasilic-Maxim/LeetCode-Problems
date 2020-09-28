from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = 0
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                if product >= k:
                    break
                counter += 1
        return counter
