from typing import List


class Solution:
    """
    Time: O(2n) => O(n)
    Space: O(1)
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        counter = slow = 0
        for fast, num in enumerate(nums):
            product *= num
            while product >= k:
                product //= nums[slow]
                slow += 1

            counter += fast - slow + 1
        return counter
