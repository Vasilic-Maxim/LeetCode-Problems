from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binary_search(nums, target)
        return [start, self.binary_search(nums, target + 1) - 1] if target in nums[start:start + 1] else [-1, -1]

    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        return left
