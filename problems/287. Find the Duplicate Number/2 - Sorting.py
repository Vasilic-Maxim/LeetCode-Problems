from typing import List


class Solution:
    """
    NOTE:
        You must not modify the array (assume the array is read only).
        You must use only constant, O(1) extra space.

    In any case sorting consumes non constant memory.

    Time: O(n * log (n))
    Space: O(n)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
