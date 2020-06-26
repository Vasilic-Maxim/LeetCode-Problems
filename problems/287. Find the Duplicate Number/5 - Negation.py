from typing import List


class Solution:
    """
    NOTE:
        You must not modify the array (assume the array is read only).

    Time: O(n)
    Space: O(n)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            else:
                nums[abs(num) - 1] *= -1