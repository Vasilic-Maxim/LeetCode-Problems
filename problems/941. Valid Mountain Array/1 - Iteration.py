from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def validMountainArray(self, nums: List[int]) -> bool:
        i = 0
        while i + 1 < len(nums) and nums[i] < nums[i + 1]:
            i += 1

        if not (0 < i < len(nums) - 1):
            return False

        while i + 1 < len(nums) and nums[i] < nums[i + 1]:
            i += 1

        return i + 1 == len(nums)
