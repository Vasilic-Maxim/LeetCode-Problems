from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = -1, 1
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1

        return [dup, missing]
