from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 1
        result = []
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                result.append(nums[i])
                i += 2
            else:
                i += 1
        return result
