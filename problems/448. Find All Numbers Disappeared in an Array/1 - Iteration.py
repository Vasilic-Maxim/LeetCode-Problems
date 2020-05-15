from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_map = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in nums_map]
