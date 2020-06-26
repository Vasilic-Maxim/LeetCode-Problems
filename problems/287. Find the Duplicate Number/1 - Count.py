from typing import List


class Solution:
    """
    NOTE:
        Your runtime complexity should be less than O(n ** 2).

    Time: O(n ** 2)
    Space: O(1)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > 1:
                return num
