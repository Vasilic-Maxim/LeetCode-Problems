from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = missing = 0
        for num in range(1, len(nums) + 1):
            count = nums.count(num)
            if count == 2:
                dup = num
            elif count == 0:
                missing = num

            if dup and missing:
                return [dup, missing]
